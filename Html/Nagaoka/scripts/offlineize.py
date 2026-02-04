#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import re
from pathlib import Path
from urllib.parse import SplitResult, urlsplit


ALLOWED_HOSTS = {
    "nagaoka-fudousan-satei.com",
    "www.nagaoka-fudousan-satei.com",
}

STATIC_PATH_PREFIXES = (
    "/wp-content/",
    "/wp-includes/",
)

STATIC_EXTENSIONS = (
    ".css",
    ".js",
    ".mjs",
    ".json",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".svg",
    ".webp",
    ".ico",
    ".woff",
    ".woff2",
    ".ttf",
    ".eot",
    ".otf",
    ".map",
)


def _posix_relpath(target: Path, start: Path) -> str:
    return Path(os.path.relpath(target, start=start)).as_posix()


def _is_static_path(url_path: str) -> bool:
    lower = url_path.lower()
    if lower.startswith(STATIC_PATH_PREFIXES):
        return True
    return lower.endswith(STATIC_EXTENSIONS)


def _parse_urlish(value: str) -> SplitResult:
    # wget --convert-links sometimes URL-encodes query delimiters into the path
    # (e.g. `app.js%3Fver=1.2.3`), which breaks offline serving. Normalize back
    # to a standard query string so we can strip it and map to local files.
    value = re.sub(r"%3[fF]", "?", value)
    if value.startswith("//"):
        return urlsplit("https:" + value)
    return urlsplit(value)


def _local_target_for_url_path(site_dir: Path, url_path: str) -> Path | None:
    if not url_path:
        return None

    if url_path == "/":
        return site_dir / "index.html"

    rel = url_path.lstrip("/")
    direct = site_dir / rel
    if direct.is_file():
        return direct

    # Many permalinks are stored as /path/index.html.
    if direct.is_dir():
        index_html = direct / "index.html"
        if index_html.is_file():
            return index_html

    # Some permalinks are stored as /path.html (e.g. when the original URL
    # lacked a trailing slash or wget used a file-based naming strategy).
    rel_no_slash = rel.rstrip("/")
    if rel_no_slash and "." not in Path(rel_no_slash).name:
        html = site_dir / (rel_no_slash + ".html")
        if html.is_file():
            return html

    return None


def _rewrite_link_value(site_dir: Path, current_file: Path, value: str) -> str:
    if not value or value.startswith(("data:", "mailto:", "tel:", "javascript:")):
        return value

    parsed = _parse_urlish(value)

    url_path = parsed.path
    if parsed.scheme in ("http", "https"):
        if parsed.netloc.lower() not in ALLOWED_HOSTS:
            return value
    elif value.startswith("/"):
        pass
    else:
        # Relative URL: only strip query for static assets.
        if parsed.query and _is_static_path(url_path):
            return url_path + (("#" + parsed.fragment) if parsed.fragment else "")
        if parsed.query == "" and "?" in value and _is_static_path(url_path):
            # Handles URLs like *.eot?#iefix -> *.eot#iefix
            return url_path + (("#" + parsed.fragment) if parsed.fragment else "")
        return value

    # For absolute/root-relative URLs, drop query for static assets.
    local_url_path = url_path or "/"
    if _is_static_path(local_url_path) or parsed.query:
        fragment = ("#" + parsed.fragment) if parsed.fragment else ""
        target = _local_target_for_url_path(site_dir, local_url_path)
        if target is None:
            return local_url_path + fragment
        return _posix_relpath(target, start=current_file.parent) + fragment

    fragment = ("#" + parsed.fragment) if parsed.fragment else ""
    target = _local_target_for_url_path(site_dir, local_url_path)
    if target is None:
        return value
    return _posix_relpath(target, start=current_file.parent) + fragment


HTML_ATTR_RE = re.compile(
    r"""(?P<attr>\b(?:href|src)\b)\s*=\s*(?P<q>["'])(?P<val>[^"']+)(?P=q)""",
    re.IGNORECASE,
)

CSS_URL_RE = re.compile(
    r"""url\(\s*(?P<q>["']?)(?P<val>[^"'()]+)(?P=q)\s*\)""",
    re.IGNORECASE,
)

CSS_IMPORT_RE = re.compile(
    r"""@import\s+(?:url\(\s*(?P<uq>["']?)(?P<uval>[^"'()]+)(?P=uq)\s*\)|(?P<q>["'])(?P<val>[^"']+)(?P=q))""",
    re.IGNORECASE,
)


def _rewrite_html_file(site_dir: Path, html_path: Path) -> bool:
    original = html_path.read_text(encoding="utf-8", errors="ignore")

    def repl(match: re.Match[str]) -> str:
        attr = match.group("attr")
        q = match.group("q")
        val = match.group("val")
        new_val = _rewrite_link_value(site_dir, html_path, val)
        return f"{attr}={q}{new_val}{q}"

    updated = HTML_ATTR_RE.sub(repl, original)
    if updated == original:
        return False
    html_path.write_text(updated, encoding="utf-8")
    return True


def _rewrite_css_file(site_dir: Path, css_path: Path) -> bool:
    original = css_path.read_text(encoding="utf-8", errors="ignore")

    def url_repl(match: re.Match[str]) -> str:
        q = match.group("q") or ""
        val = match.group("val")
        new_val = _rewrite_link_value(site_dir, css_path, val)
        return f"url({q}{new_val}{q})"

    updated = CSS_URL_RE.sub(url_repl, original)

    def import_repl(match: re.Match[str]) -> str:
        if match.group("uval") is not None:
            q = match.group("uq") or ""
            val = match.group("uval")
            new_val = _rewrite_link_value(site_dir, css_path, val)
            return f"@import url({q}{new_val}{q})"
        q = match.group("q")
        val = match.group("val")
        new_val = _rewrite_link_value(site_dir, css_path, val)
        return f"@import {q}{new_val}{q}"

    updated = CSS_IMPORT_RE.sub(import_repl, updated)

    if updated == original:
        return False
    css_path.write_text(updated, encoding="utf-8")
    return True


def normalize_query_filenames(site_dir: Path) -> int:
    renamed = 0
    for path in sorted(site_dir.rglob("*"), key=lambda p: len(str(p)), reverse=True):
        if not path.is_file():
            continue
        if "?" not in path.name:
            continue

        new_name = path.name.split("?", 1)[0]
        new_path = path.with_name(new_name)
        if new_path == path:
            continue
        if new_path.exists():
            if path.stat().st_size == new_path.stat().st_size and path.read_bytes() == new_path.read_bytes():
                path.unlink()
                continue
            backup_path = new_path.with_name(new_name + ".query_backup")
            if backup_path.exists():
                raise RuntimeError(f"Refusing to overwrite existing file: {backup_path}")
            path.rename(backup_path)
            renamed += 1
            continue
        path.rename(new_path)
        renamed += 1
    return renamed


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Make mirrored site work offline (strip query filenames and rewrite links)."
    )
    parser.add_argument("--site-dir", default="site", help="Directory containing mirrored site (default: site)")
    args = parser.parse_args()

    site_dir = Path(args.site_dir).resolve()
    if not site_dir.is_dir():
        raise SystemExit(f"site dir not found: {site_dir}")

    renamed = normalize_query_filenames(site_dir)
    print(f"renamed querystring files: {renamed}")

    changed = 0
    for html_path in site_dir.rglob("*.html"):
        if _rewrite_html_file(site_dir, html_path):
            changed += 1
    for css_path in site_dir.rglob("*.css"):
        if _rewrite_css_file(site_dir, css_path):
            changed += 1
    print(f"rewritten files: {changed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
