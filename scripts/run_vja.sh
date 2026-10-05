#!/usr/bin/env bash
# VJA / IESBench main evaluation (ICML 2026).
# MODE=attack  -> undefended Qwen-Image-Edit on 1054 IESBench images
# MODE=defense -> introspective Qwen-Image-Edit-Safe
# Optional: MAX_SAMPLES=2 for a smoke run
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
export PYTHONPATH="${ROOT}:${PYTHONPATH:-}"
MODE="${MODE:-attack}"
if [[ "${MODE}" == "defense" ]]; then
  CONFIG="${ROOT}/configs/vja/main_defense.yaml"
else
  CONFIG="${ROOT}/configs/vja/main_attack.yaml"
fi
EXTRA=()
if [[ -n "${MAX_SAMPLES:-}" ]]; then
  EXTRA+=(--max-samples "${MAX_SAMPLES}")
fi
python "${ROOT}/scripts/run.py" vja --config "${CONFIG}" "${EXTRA[@]}"
