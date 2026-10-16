#!/usr/bin/env bash
# Make one Short from a topic:            ./make-video.sh "5 facts about chai"
# Use your own recorded narration:        VOICE_FILE=me.mp3 ./make-video.sh "topic" "full script text"
# Extra CLI options go after the topic/script, e.g. --video-aspect 16:9 (see --help).
set -euo pipefail
cd "$(dirname "$0")/tools/MoneyPrinterTurbo"
case "${1:-}" in -h|--help) exec .venv/bin/python cli.py --help;; esac
topic="${1:?usage: make-video.sh \"topic\" [script] [extra options]}"; shift
args=(--video-subject "$topic")
if [ $# -gt 0 ] && [[ "$1" != --* ]]; then args+=(--video-script "$1"); shift; fi
if [ -n "${VOICE_FILE:-}" ]; then args+=(--custom-audio-file "$(cd - >/dev/null; realpath "$VOICE_FILE")"); fi
exec .venv/bin/python cli.py "${args[@]}" "$@"
