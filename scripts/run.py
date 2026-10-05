from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from core.config import load_config
from core.registry import get_adapter


def main() -> None:
    parser = argparse.ArgumentParser(description="I2Isafe unified runner (attacks/*.run)")
    parser.add_argument("method", help="advi2i | coljailbreak | mma_diffusion | mfj | vja")
    parser.add_argument("-c", "--config", required=True, help="YAML config under configs/")
    parser.add_argument("--stage", default=None, help="override config.stage")
    parser.add_argument("--max-samples", type=int, default=None)
    args = parser.parse_args()

    cfg = load_config(args.config)
    if args.stage:
        cfg["stage"] = args.stage
    if args.max_samples is not None:
        cfg["max_samples"] = args.max_samples
    cfg.setdefault("method", args.method)
    run = get_adapter(args.method)
    run(cfg)


if __name__ == "__main__":
    main()
