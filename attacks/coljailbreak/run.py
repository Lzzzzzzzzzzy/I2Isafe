from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

from core.paths import DATASET_DIRS, OUTPUT_ROOT

_PKG = Path(__file__).resolve().parent


def run(cfg: dict) -> None:
    if str(_PKG) not in sys.path:
        sys.path.insert(0, str(_PKG))
    from pipeline import main as pipeline_main

    data_dir = Path(cfg.get("dataset_dir", DATASET_DIRS["coljailbreak"]))
    prompt_file = Path(cfg.get("prompt_file", data_dir / "prompts" / "main.jsonl"))
    output_dir = Path(cfg.get("output_dir", OUTPUT_ROOT / "coljailbreak" / cfg.get("experiment", "main")))
    output_dir.mkdir(parents=True, exist_ok=True)

    h = cfg.get("hparams", {})
    pool = int(h.get("substitution_pool_size", 10))
    sam_ckpt = h.get("sam_ckpt", str(data_dir / "sam_vit_h_4b8939.pth"))
    api_key = h.get("openai_api_key") or os.environ.get("OPENAI_API_KEY", "")
    if not api_key or api_key == "YOUR_OPENAI_KEY":
        raise RuntimeError(
            "ColJailBreak needs OPENAI_API_KEY (GPT-4o substitution + DALL·E as in the official pipeline)."
        )
    if not Path(sam_ckpt).exists():
        raise FileNotFoundError(f"SAM checkpoint not found: {sam_ckpt}. Run scripts/download_datasets.py first.")

    prompts = []
    if prompt_file.exists():
        with open(prompt_file, "r", encoding="utf-8") as handle:
            for line in handle:
                line = line.strip()
                if line:
                    prompts.append(json.loads(line))
    if not prompts:
        raise FileNotFoundError(f"No prompts in {prompt_file}")

    max_samples = cfg.get("max_samples")
    if max_samples:
        prompts = prompts[: int(max_samples)]

    for idx, item in enumerate(prompts):
        sample_out = output_dir / f"{idx:04d}_{item.get('category', 'unk')}"
        sample_out.mkdir(parents=True, exist_ok=True)
        args = argparse.Namespace(
            unsafe_prompt=item["unsafe_prompt"],
            unsafe_word=item["unsafe_word"],
            substitution_pool_size=pool,
            key=api_key,
            sam_ckpt=sam_ckpt,
            output_dir=str(sample_out),
        )
        print(f"[coljailbreak] {idx+1}/{len(prompts)} word={item['unsafe_word']!r}")
        pipeline_main(args)
