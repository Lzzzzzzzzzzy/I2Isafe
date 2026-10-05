#!/usr/bin/env bash
# MMA-Diffusion main experiments (CVPR 2024).
# MODE=image  -> Table 3 image-modal attack (l2=16, 20 iters, 8 SD steps)
# MODE=textual -> README text-modal attack (seed 7867, 1000 iters, 10 cands)
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
export PYTHONPATH="${ROOT}:${PYTHONPATH:-}"
MODE="${MODE:-textual}"
if [[ "${MODE}" == "textual" ]]; then
  CONFIG="${ROOT}/configs/mma_diffusion/textual.yaml"
else
  CONFIG="${ROOT}/configs/mma_diffusion/image.yaml"
fi
python "${ROOT}/scripts/run.py" mma_diffusion --config "${CONFIG}"
