#!/usr/bin/env bash
# Baja un video público (Instagram, TikTok, YouTube) a 2-referencias/videos/ para analizarlo.
# Nunca usa cookies ni tu sesión. Solo para analizar: no se vuelve a subir.
#   scripts/bajar.sh "<link>"                 # baja el video
#   scripts/bajar.sh --datos "<link>"         # solo los datos (likes, comentarios, texto, fecha; vistas solo en YouTube/TikTok)
#   scripts/bajar.sh "<link>" perfil/referencias   # baja a otra carpeta
set -euo pipefail
cd "$(dirname "$0")/.."
command -v yt-dlp >/dev/null || { echo "Falta yt-dlp: brew install yt-dlp"; exit 1; }
SEG=(--ignore-config --no-exec --no-cookies --no-cookies-from-browser --downloader native)
if [[ "${1:-}" == "--datos" ]]; then
  [[ "${2:-}" =~ ^https:// ]] || { echo "Pasá un link https://"; exit 1; }
  yt-dlp "${SEG[@]}" --skip-download --dump-single-json --flat-playlist "$2" </dev/null
  exit 0
fi
URL="${1:-}"; DEST="${2:-2-referencias/videos}"
[[ "$URL" =~ ^https:// ]] || { echo "Pasá un link https://"; exit 1; }
mkdir -p "$DEST"
yt-dlp "${SEG[@]}" --no-playlist -o "$DEST/%(id)s.%(ext)s" "$URL" </dev/null
