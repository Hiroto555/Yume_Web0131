#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import shutil
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Rule:
    name: str
    pattern: re.Pattern[str]
    replacement: str = ""


FLAGS = re.IGNORECASE | re.DOTALL

EXTERNAL_SERVICE_DOMAINS_RE = r"(?:nagaoka-fudousan\.com|nagaoka-f\.com|niigata-kaitori\.com|bn-housing\.jp)"

RULES: list[Rule] = [
    # Related/affiliate services section (external links).
    Rule(
        name="Remove footer related-services section",
        pattern=re.compile(r'<section\b[^>]*class=["\'][^"\']*\bft-bnr\b[^"\']*["\'][^>]*>.*?</section>\s*', FLAGS),
    ),
    Rule(
        name="Remove external service links",
        pattern=re.compile(rf'<a\b[^>]*\bhref=["\']https?://{EXTERNAL_SERVICE_DOMAINS_RE}[^"\']*["\'][^>]*>.*?</a>', FLAGS),
    ),
    # External font loaders.
    Rule(
        name="Remove FontPlus loader",
        pattern=re.compile(r'<script\b[^>]*\bsrc=["\'][^"\']*webfont\.fontplus\.jp[^"\']*["\'][^>]*>.*?</script>\s*', FLAGS),
    ),
    Rule(
        name="Remove Google Fonts stylesheet",
        pattern=re.compile(r'<link\b[^>]*\bhref=["\'][^"\']*fonts\.googleapis\.com[^"\']*["\'][^>]*>\s*', FLAGS),
    ),
    Rule(
        name="Remove Google Fonts preconnect/dns-prefetch",
        pattern=re.compile(r'<link\b[^>]*\bhref=["\'](?:https?:)?//fonts\.(?:googleapis|gstatic)\.com[^"\']*["\'][^>]*>\s*', FLAGS),
    ),
    Rule(
        name="Remove FontPlus preconnect/dns-prefetch",
        pattern=re.compile(r'<link\b[^>]*\bhref=["\'](?:https?:)?//webfont\.fontplus\.jp[^"\']*["\'][^>]*>\s*', FLAGS),
    ),
    # Yoast SEO artifacts (exposes original site metadata).
    Rule(
        name="Remove Yoast SEO optimization comment",
        pattern=re.compile(r"<!--\s*This site is optimized with the Yoast SEO plugin.*?-->\s*", FLAGS),
    ),
    Rule(
        name="Remove Yoast schema graph JSON-LD",
        pattern=re.compile(r'<script\b[^>]*class=["\']yoast-schema-graph["\'][^>]*>.*?</script>\s*', FLAGS),
    ),
    Rule(
        name="Remove Yoast SEO footer comment",
        pattern=re.compile(r"<!--\s*/\s*Yoast SEO plugin\.\s*-->\s*", FLAGS),
    ),
    # Meta/link tags that hardcode the original domain.
    Rule(
        name="Remove meta tags referencing original domain",
        pattern=re.compile(r'<meta\b[^>]*\bcontent=["\'][^"\']*nagaoka-fudousan-satei\.com[^"\']*["\'][^>]*>\s*', FLAGS),
    ),
    Rule(
        name="Remove link tags referencing original domain",
        pattern=re.compile(r'<link\b[^>]*\bhref=["\']https?://nagaoka-fudousan-satei\.com[^"\']*["\'][^>]*>\s*', FLAGS),
    ),
    # Google Analytics / Ads (gtag) blocks.
    Rule(
        name="Remove gtag.js loader",
        pattern=re.compile(r'<script\b[^>]*\bsrc=["\']https://www\.googletagmanager\.com/gtag/js[^"\']*["\'][^>]*>.*?</script>\s*', FLAGS),
    ),
    Rule(
        name="Remove GA/Ads wrapper comments (▼/▲)",
        pattern=re.compile(r"<!--\s*▼\s*Google Analytics\s*▼\s*-->.*?<!--\s*▲\s*Google Analytics\s*▲\s*-->\s*", FLAGS),
    ),
    Rule(
        name="Remove gtag inline config script",
        pattern=re.compile(r"<script\b[^>]*>\s*window\.dataLayer\s*=.*?gtag\('config'.*?</script>\s*", FLAGS),
    ),
    Rule(
        name="Remove Google Ads conversion event snippet",
        pattern=re.compile(r"<script\b[^>]*>\s*gtag\('event'\s*,\s*'conversion'.*?</script>\s*", FLAGS),
    ),
    # Google Tag Manager blocks.
    Rule(
        name="Remove GTM inline loader",
        pattern=re.compile(r"<script\b[^>]*>\s*\(function\(w,\s*d,\s*s,\s*l,\s*i\)\s*\{.*?googletagmanager\.com/gtm\.js.*?\}\)\(window,\s*document,\s*'script',\s*'dataLayer',\s*'GTM-[A-Z0-9]+'\);\s*</script>\s*", FLAGS),
    ),
    Rule(
        name="Remove GTM comments (head/body)",
        pattern=re.compile(r"<!--\s*Google Tag Manager(?:\s*\(noscript\))?\s*-->.*?<!--\s*End Google Tag Manager(?:\s*\(noscript\))?\s*-->\s*", FLAGS),
    ),
    Rule(
        name="Remove GTM noscript iframe",
        pattern=re.compile(r"<noscript>\s*<iframe\b[^>]*googletagmanager\.com/ns\.html[^>]*></iframe>\s*</noscript>\s*", FLAGS),
    ),
    # reCAPTCHA (CF7 integration).
    Rule(
        name="Remove reCAPTCHA API loader",
        pattern=re.compile(r'<script\b[^>]*\bsrc=["\']https://www\.google\.com/recaptcha/api\.js[^"\']*["\'][^>]*>.*?</script>\s*', FLAGS),
    ),
    Rule(
        name="Remove CF7 reCAPTCHA config block",
        pattern=re.compile(r'<script\b[^>]*\bid=["\']wpcf7-recaptcha-js-before["\'][^>]*>.*?</script>\s*', FLAGS),
    ),
    Rule(
        name="Remove CF7 reCAPTCHA module script tag",
        pattern=re.compile(r'<script\b[^>]*\bsrc=["\'][^"\']*contact-form-7/modules/recaptcha/index\.js[^"\']*["\'][^>]*>.*?</script>\s*', FLAGS),
    ),
    Rule(
        name="Remove CF7 reCAPTCHA hidden input",
        pattern=re.compile(r'<input\b[^>]*\bname=["\']_wpcf7_recaptcha_response["\'][^>]*>\s*', FLAGS),
    ),
    # Yahoo conversion pixel/snippet (thank you page).
    Rule(
        name="Remove Yahoo conversion inline snippet",
        pattern=re.compile(r"<script\b[^>]*>.*?yahoo_conversion_id\s*=.*?</script>\s*", FLAGS),
    ),
    Rule(
        name="Remove Yahoo conversion script tag",
        pattern=re.compile(r'<script\b[^>]*\bsrc=["\']https://s\.yimg\.jp/images/listing/tool/cv/conversion\.js["\'][^>]*>.*?</script>\s*', FLAGS),
    ),
    Rule(
        name="Remove Yahoo conversion noscript pixel",
        pattern=re.compile(r"<noscript>\s*<div\b[^>]*>\s*<img\b[^>]*b91\.yahoo\.co\.jp/pagead/conversion/[^>]*>\s*</div>\s*</noscript>\s*", FLAGS),
    ),
]


SCRIPT_BLOCK_RE = re.compile(r"<script\b[^>]*>.*?</script>", FLAGS)
NOSCRIPT_BLOCK_RE = re.compile(r"<noscript\b[^>]*>.*?</noscript>", FLAGS)

INLINE_BAD_MARKERS = [
    # GTM / GA / Ads
    "gtm-mtmgfhnj",
    "ua-128506951-48",
    "g-0218nrtkk3",
    "aw-10940613225",
    "googletagmanager.com",
    "gtag(",
    "datalayer",
    # reCAPTCHA
    "grecaptcha",
    "wpcf7_recaptcha",
    "google.com/recaptcha",
    # Yahoo conversion
    "yahoo_conversion_id",
    "s.yimg.jp/images/listing/tool/cv/conversion.js",
    "b91.yahoo.co.jp/pagead/conversion/",
]


def _strip_inline_blocks(html: str) -> tuple[str, int]:
    removed = 0

    def script_repl(match: re.Match[str]) -> str:
        nonlocal removed
        block = match.group(0)
        lower = block.lower()
        if any(marker in lower for marker in INLINE_BAD_MARKERS):
            removed += 1
            return ""
        return block

    html = SCRIPT_BLOCK_RE.sub(script_repl, html)

    def noscript_repl(match: re.Match[str]) -> str:
        nonlocal removed
        block = match.group(0)
        lower = block.lower()
        if (
            "googletagmanager.com/ns.html" in lower
            or "gtm-" in lower
            or "b91.yahoo.co.jp/pagead/conversion/" in lower
        ):
            removed += 1
            return ""
        return block

    html = NOSCRIPT_BLOCK_RE.sub(noscript_repl, html)
    return html, removed


def clean_html(html: str) -> tuple[str, int]:
    changed = 0
    for rule in RULES:
        html, n = rule.pattern.subn(rule.replacement, html)
        if n:
            changed += n

    html, n = _strip_inline_blocks(html)
    changed += n
    return html, changed


def main() -> int:
    parser = argparse.ArgumentParser(description="Remove tracking/third-party snippets from mirrored HTML.")
    parser.add_argument("--site-dir", default="site", help="Directory containing mirrored site (default: site)")
    args = parser.parse_args()

    site_dir = Path(args.site_dir).resolve()
    if not site_dir.is_dir():
        raise SystemExit(f"site dir not found: {site_dir}")

    html_files = sorted(site_dir.rglob("*.html"))
    files_changed = 0
    total_edits = 0
    for path in html_files:
        original = path.read_text(encoding="utf-8", errors="ignore")
        cleaned, edits = clean_html(original)
        if cleaned != original:
            path.write_text(cleaned, encoding="utf-8")
            files_changed += 1
            total_edits += edits

    # Remove unused local reCAPTCHA module assets (keeps the mirror cleaner and avoids stray references).
    recaptcha_module_dir = site_dir / "wp-content" / "plugins" / "contact-form-7" / "modules" / "recaptcha"
    deleted_paths: list[Path] = []
    if recaptcha_module_dir.is_dir():
        shutil.rmtree(recaptcha_module_dir)
        deleted_paths.append(recaptcha_module_dir)

    print(f"scanned html files: {len(html_files)}")
    print(f"changed files: {files_changed}")
    print(f"total removals: {total_edits}")
    if deleted_paths:
        for p in deleted_paths:
            try:
                rel = p.relative_to(site_dir)
            except ValueError:
                rel = p
            print(f"deleted: {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
