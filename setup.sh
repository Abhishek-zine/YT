#!/usr/bin/env bash
# One-time setup on your own computer (macOS/Linux). Needs git, Python 3.11+ and ffmpeg.
set -euo pipefail
cd "$(dirname "$0")"
git submodule update --init tools/MoneyPrinterTurbo
MPT=tools/MoneyPrinterTurbo
[ -f "$MPT/config.toml" ] || cp mpt/config.toml "$MPT/config.toml"
python3 -m venv "$MPT/.venv"
"$MPT/.venv/bin/pip" install -r "$MPT/requirements.txt"
echo
echo "Done. Next: put your keys in $MPT/config.toml (anthropic_api_key, pexels_api_keys),"
echo "then run ./make-video.sh \"your topic\"  or  ./webui.sh"
