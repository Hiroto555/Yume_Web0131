# HomePage_Yume (nagaoka-fudousan-satei.com mirror)

## Preview

Entry page is `site/index.html`.

Run a local server from this repo root:

```sh
python3 -m http.server 8000 --directory project2/site
```

Then open `http://localhost:8000/`.

## Fix broken CSS/JS after mirroring

If assets were downloaded with querystrings in filenames (e.g. `main.css?ver=...`), run:

```sh
python3 project2/scripts/offlineize.py --site-dir project2/site
```

This normalizes filenames and rewrites links inside `project2/site/*.html` + `project2/site/*.css` so the pages load assets locally.

## Notes

- This is a static mirror; WordPress dynamic features (forms/search/API) may not work offline.

