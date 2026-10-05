#!/usr/bin/env bash
# Gradient-based jailbreak images for multimodal fusion models.
# STAGE=train_shortcut | attack
# Direct 72.5% setting: CONFIG=configs/mfj/main_direct.yaml STAGE=attack
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
export PYTHONPATH="${ROOT}:${PYTHONPATH:-}"
STAGE="${STAGE:-train_shortcut}"
if [[ "${STAGE}" == "train_shortcut" ]]; then
  CONFIG="${CONFIG:-${ROOT}/configs/mfj/train_shortcut.yaml}"
else
  CONFIG="${CONFIG:-${ROOT}/configs/mfj/main_transfer.yaml}"
fi
python "${ROOT}/scripts/run.py" mfj --config "${CONFIG}" --stage "${STAGE}"
