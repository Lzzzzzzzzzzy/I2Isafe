#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
export PYTHONPATH="${ROOT}:${PYTHONPATH:-}"
python "${ROOT}/scripts/download_datasets.py"
