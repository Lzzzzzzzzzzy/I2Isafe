from __future__ import annotations

import argparse
import sys
from pathlib import Path

from core.paths import DATASET_DIRS, OUTPUT_ROOT
from core.runner import set_offline_logging

_PKG = Path(__file__).resolve().parent


def run(cfg: dict) -> None:
    set_offline_logging()
    data_dir = Path(cfg.get("dataset_dir", DATASET_DIRS["mma_diffusion"]))
    h = cfg.get("hparams", {})
    sd_path = h.get("sd_inpaint_path", "stable-diffusion-v1-5/stable-diffusion-inpainting")
    modality = cfg.get("modality", "image")
    output_dir = Path(cfg.get("output_dir", OUTPUT_ROOT / "mma_diffusion" / modality))
    output_dir.mkdir(parents=True, exist_ok=True)

    if modality == "textual":
        if str(_PKG) not in sys.path:
            sys.path.insert(0, str(_PKG))
        from textual_attack import main as textual_main, set_seed

        args = argparse.Namespace(
            random_seed=int(h.get("seed", 7867)),
            iteration=int(h.get("iteration", 1000)),
            candicate_number=int(h.get("candicate_number", 10)),
            sd_inpaint_path=sd_path,
            save_path=str(output_dir) + "/",
        )
        set_seed(args.random_seed)
        textual_main(args)
        return

    image_dir = data_dir / "mma_diffusion_images"
    if not image_dir.exists():
        raise FileNotFoundError(
            f"MMA image/mask pairs not found at {image_dir}. Run scripts/download_datasets.py"
        )
    attack_dir = _PKG / "image_space_attack"
    if str(attack_dir) not in sys.path:
        sys.path.insert(0, str(attack_dir))
    from image_editing_attack import main as image_main

    args = argparse.Namespace(
        iter=int(h.get("iter", 20)),
        accumulate=int(h.get("accumulate", 8)),
        epsl2=float(h.get("epsl2", 16.0)),
        epslinf=float(h.get("epslinf", 16 / 255)),
        adjustment=float(h.get("adjustment", 0.07)),
        save_path=str(output_dir) + "/",
        input_path=str(image_dir) + "/",
        inference=True,
        l2=True,
        random_seed=int(h.get("seed", 3)),
        num_inference_steps=int(h.get("num_inference_steps", 8)),
        sd_inpaint_path=sd_path,
        assets_dir=str(data_dir / "assets"),
    )
    image_main(args)
