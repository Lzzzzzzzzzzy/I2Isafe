from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from .paths import CONFIG_ROOT, DATASET_ROOT, I2ISAFE_ROOT, OUTPUT_ROOT, REPOS


def load_config(path: str | Path) -> dict[str, Any]:
    path = Path(path)
    if not path.is_absolute():
        for candidate in (path, CONFIG_ROOT / path, I2ISAFE_ROOT / path):
            if candidate.exists():
                path = candidate
                break
    with open(path, "r", encoding="utf-8") as handle:
        cfg = yaml.safe_load(handle) or {}
    cfg["_config_path"] = str(path.resolve())
    return resolve_config(cfg)


def resolve_config(cfg: dict[str, Any]) -> dict[str, Any]:
    tokens = {
        "I2ISAFE_ROOT": str(I2ISAFE_ROOT),
        "I2ISAFE_DATA": str(DATASET_ROOT),
        "I2ISAFE_OUT": str(OUTPUT_ROOT),
        "ADVI2I_REPO": str(REPOS["advi2i"]),
        "COLJAIL_REPO": str(REPOS["coljailbreak"]),
        "MMA_REPO": str(REPOS["mma_diffusion"]),
        "MFJ_REPO": str(REPOS["mfj"]),
        "VJA_REPO": str(REPOS["vja"]),
    }

    def _resolve(value: Any) -> Any:
        if isinstance(value, str):
            for key, replacement in tokens.items():
                value = value.replace("${" + key + "}", replacement)
            return value
        if isinstance(value, list):
            return [_resolve(item) for item in value]
        if isinstance(value, dict):
            return {k: _resolve(v) for k, v in value.items()}
        return value

    return _resolve(cfg)
