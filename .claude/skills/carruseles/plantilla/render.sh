#!/usr/bin/env bash
# Pasa cada slide-XX.html de esta carpeta a PNG (1080×1350) con Google Chrome.
set -euo pipefail
cd "$(dirname "$0")"
CH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
[[ -x "$CH" ]] || CH="$(command -v google-chrome || command -v chromium || true)"
[[ -n "$CH" ]] || { echo "Falta Google Chrome"; exit 1; }
for f in slide-*.html; do
  "$CH" --headless=new --disable-gpu --hide-scrollbars --window-size=1080,1350 \
    --virtual-time-budget=4000 --screenshot="${f%.html}.png" "file://$PWD/$f" >/dev/null 2>&1
  echo "${f%.html}.png"
done
