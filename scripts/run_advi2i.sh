#!/usr/bin/env bash
# AdvI2I main experiment: NSFW steering vector + VAE generator on SD-1.5-Inpaint.
# Paper: ICML 2025. Default recipe from the official README / Table 4 setting (eps=64/255).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
export PYTHONPATH="${ROOT}:${PYTHONPATH:-}"
STAGE="${STAGE:-all}"
CONFIG="${CONFIG:-${ROOT}/configs/advi2i/main_inpaint.yaml}"
python "${ROOT}/scripts/run.py" advi2i --config "${CONFIG}" --stage "${STAGE}"

# 56.0