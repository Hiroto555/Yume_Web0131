#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
theme_dir="$(cd "$script_dir/.." && pwd)"
theme_name="$(basename "$theme_dir")"
parent_dir="$(cd "$theme_dir/.." && pwd)"
output_zip="$parent_dir/${theme_name}.zip"

cd "$parent_dir"
rm -f "$output_zip"
zip -r "$output_zip" "$theme_name" -x "*.DS_Store" -x "**/.DS_Store"
echo "Created: $output_zip"

