from __future__ import annotations

import sys
from pathlib import Path

from core.paths import DATASET_DIRS, OUTPUT_ROOT
from core.runner import set_offline_logging

_PKG = Path(__file__).resolve().parent


def _ensure_libpath() -> None:
    path = str(_PKG)
    if path not in sys.path:
        sys.path.insert(0, path)


def _argv_from_hparams(h: dict) -> list[str]:
    argv: list[str] = []
    mapping = [
        ("ddim_steps", "--ddim_steps"),
        ("tar_steps", "--tar_steps"),
        ("strength", "--strength"),
        ("vec_scale", "--vec_scale"),
        ("concept", "--concept"),
        ("mask_dir", "--mask_dir"),
        ("version", "--version"),
        ("dtype", "--dtype"),
        ("epoch", "--epoch"),
        ("lr", "--lr"),
        ("eps", "--eps"),
        ("loss_type", "--loss_type"),
        ("prefix", "--prefix"),
        ("bs", "--bs"),
        ("resolution", "--resolution"),
        ("seed", "--seed"),
        ("device", "--device"),
        ("ckpt", "--ckpt"),
    ]
    for key, flag in mapping:
        if key in h and h[key] not in (None, ""):
            argv.extend([flag, str(h[key])])
    return argv


def run(cfg: dict) -> None:
    set_offline_logging()
    _ensure_libpath()
    from settings import set_work_path
    from utils.util import get_args

    work = Path(cfg.get("dataset_dir", DATASET_DIRS["advi2i"]))
    set_work_path(work)
    output = Path(cfg.get("output_dir", OUTPUT_ROOT / "advi2i" / cfg.get("experiment", "main")))
    output.mkdir(parents=True, exist_ok=True)

    args = get_args(_argv_from_hparams(cfg.get("hparams", {})))
    stage = cfg.get("stage", "all")
    family = cfg.get("family", "inpaint")

    if stage in ("vec", "all"):
        print("[advi2i] generating NSFW steering vector")
        import vec_gen
        vec_gen.main(args)
    if stage in ("train", "all"):
        if family == "p2p":
            import opt_generator_p2p as train_mod
        else:
            import opt_generator_inpaint as train_mod
        print(f"[advi2i] training generator via {train_mod.__name__}")
        train_mod.main(args)
    if stage == "eval":
        if family == "p2p":
            import eval_generator_p2p as eval_mod
        else:
            import eval_generator_inpaint as eval_mod
        print(f"[advi2i] evaluating via {eval_mod.__name__}")
        eval_mod.main(args)
    print(f"[advi2i] work_path={work} output_dir={output}")
