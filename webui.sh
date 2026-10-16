#!/usr/bin/env bash
# Opens MoneyPrinterTurbo's browser UI at http://127.0.0.1:8501
set -euo pipefail
cd "$(dirname "$0")/tools/MoneyPrinterTurbo"
exec .venv/bin/python -m streamlit run ./webui/Main.py --browser.gatherUsageStats=False --server.address 127.0.0.1
