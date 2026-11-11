#!/usr/bin/env bash
# Render every script in a series folder as one Short each, in English with a US male voice.
#   ./make-series.sh series/jensen-huang-si
#   ./make-series.sh series/jensen-huang-si --video-aspect 16:9     # extra options pass through
# Each NN-name.txt is the exact narration; the topic is taken from the file name.
set -euo pipefail
cd "$(dirname "$0")"
dir="${1:?usage: make-series.sh <series folder> [extra make-video.sh options]}"; shift
for f in "$dir"/[0-9]*.txt; do
  topic="$(basename "$f" .txt | sed 's/^[0-9]*-//; s/-/ /g')"
  echo "== $topic"
  ./make-video.sh "$topic" "$(cat "$f")" \
    --video-language en-US --voice-name en-US-AndrewNeural-Male --voice-rate 1.1 "$@"
done
