#!/usr/bin/env bash
# ColJailBreak main experiment (NeurIPS 2024): |S|=10, I2P-derived prompts, SAM + inpainting.
# Requires OPENAI_API_KEY. Optional: MAX_SAMPLES=1 for a smoke run.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
export PYTHONPATH="${ROOT}:${PYTHONPATH:-}"
CONFIG="${CONFIG:-${ROOT}/configs/coljailbreak/main.yaml}"
EXTRA=()
if [[ -n "${MAX_SAMPLES:-}" ]]; then
  EXTRA+=(--max-samples "${MAX_SAMPLES}")
fi
python "${ROOT}/scripts/run.py" coljailbreak --config "${CONFIG}" "${EXTRA[@]}"
