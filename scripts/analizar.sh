#!/usr/bin/env bash
# Prepara un video para que Claude lo mire: transcripción con tiempos + un cuadro cada 2 s.
#   scripts/analizar.sh 2-referencias/videos/<id>.mp4 [idioma]   (idioma: es, en, auto; por defecto auto)
# Sale en .tmp/<id>/: audio.wav, transcripcion.txt (+ .srt) y cuadros/c_001.jpg …
set -euo pipefail
cd "$(dirname "$0")/.."
V="$1"; LANG_W="${2:-auto}"
[[ -f "$V" ]] || { echo "No existe $V"; exit 1; }
command -v ffmpeg >/dev/null || { echo "Falta ffmpeg: brew install ffmpeg"; exit 1; }
command -v whisper-cli >/dev/null || { echo "Falta whisper: brew install whisper-cpp"; exit 1; }
MOD="$HOME/.cache/whisper/ggml-small.bin"
if [[ ! -f "$MOD" ]]; then
  mkdir -p "$(dirname "$MOD")"
  echo "Bajando el modelo de whisper (una sola vez, ~470 MB)…"
  curl -L --fail -o "$MOD" https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-small.bin
fi
ID="$(basename "${V%.*}")"; OUT=".tmp/$ID"; mkdir -p "$OUT/cuadros"
ffmpeg -nostdin -loglevel error -y -i "$V" -ar 16000 -ac 1 "$OUT/audio.wav"
whisper-cli -m "$MOD" -l "$LANG_W" -f "$OUT/audio.wav" -otxt -osrt -of "$OUT/transcripcion" >/dev/null 2>&1
ffmpeg -nostdin -loglevel error -y -i "$V" -vf "fps=1/2,scale=540:-2" "$OUT/cuadros/c_%03d.jpg"
echo "Listo: $OUT/transcripcion.txt y $(ls "$OUT/cuadros" | wc -l | tr -d ' ') cuadros en $OUT/cuadros/"
