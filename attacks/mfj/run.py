from __future__ import annotations

import os
import sys
from pathlib import Path

import yaml

from core.paths import DATASET_DIRS, OUTPUT_ROOT
from core.runner import set_offline_logging

_PKG = Path(__file__).resolve().parent
_FJ = _PKG / "fusion_jailbreaks"


def run(cfg: dict) -> None:
    set_offline_logging()
    data_dir = Path(cfg.get("dataset_dir", DATASET_DIRS["mfj"]))
    data_dir.mkdir(parents=True, exist_ok=True)
    (data_dir / "data" / "models").mkdir(parents=True, exist_ok=True)
    (data_dir / "data" / "results").mkdir(parents=True, exist_ok=True)
    (data_dir / "hf_cache").mkdir(exist_ok=True)
    os.environ["I2ISAFE_MFJ_ROOT"] = str(data_dir)
    os.environ.setdefault("HF_DATASETS_CACHE", str(data_dir / "hf_cache"))

    config_file = cfg.get("upstream_config")
    if not config_file:
        raise ValueError("MFJ config needs upstream_config pointing at a method yaml")
    config_path = Path(config_file)
    if not config_path.exists():
        alt = Path(cfg["_config_path"]).parent / config_file
        config_path = alt if alt.exists() else config_path
    if not config_path.exists():
        raise FileNotFoundError(config_file)

    if str(_FJ) not in sys.path:
        sys.path.insert(0, str(_FJ))

    with open(config_path, "r", encoding="utf-8") as handle:
        config_dict = yaml.safe_load(handle) or {}

    stage = cfg.get("stage", "attack")
    old_cwd = Path.cwd()
    try:
        os.chdir(data_dir)
        if stage == "train_shortcut":
            from train import ConfigClass, main as train_main

            config = ConfigClass(**{k: v for k, v in config_dict.items() if k in ConfigClass.__dataclass_fields__})
            config.experiment_name = config_path.stem
            train_main(config, str(config_path))
        else:
            from config import ConfigClass
            from run_attack import main as attack_main

            fields = ConfigClass.__dataclass_fields__
            config = ConfigClass(**{k: v for k, v in config_dict.items() if k in fields})
            config.experiment_name = config_path.stem
            ckpt = Path(config.shortcut_checkpoint)
            if config.shortcut_checkpoint and not ckpt.is_absolute():
                config.shortcut_checkpoint = str(data_dir / config.shortcut_checkpoint)
            attack_main(config, str(config_path))
    finally:
        os.chdir(old_cwd)
    print(f"[mfj] outputs under {data_dir} and {OUTPUT_ROOT / 'mfj'}")
