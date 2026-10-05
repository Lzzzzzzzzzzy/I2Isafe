from __future__ import annotations

import json
from pathlib import Path

import torch
from PIL import Image

from core.paths import DATASET_DIRS, OUTPUT_ROOT

from .models.qwen_image_edit_safe import QwenImageEditSafePipeline, SafetyError


def _resolve_image(data_dir: Path, item: dict) -> Path:
    raw = item.get("image-path") or item.get("image_path") or ""
    stem = Path(raw).name if raw else f"{int(item['image_id']):04d}.png"
    for candidate in (
        data_dir / "img" / stem,
        data_dir / "image" / stem,
        data_dir / raw,
    ):
        if candidate.exists():
            return candidate
    padded = f"{int(item['image_id']):04d}.png"
    fallback = data_dir / "img" / padded
    if fallback.exists():
        return fallback
    raise FileNotFoundError(f"IESBench image not found for {item.get('image_id')}: {raw}")


def run(cfg: dict) -> None:
    from diffusers import QwenImageEditPlusPipeline
    from transformers import AutoModelForImageTextToText

    data_dir = Path(cfg.get("dataset_dir", DATASET_DIRS["vja"]))
    ann_path = Path(cfg.get("annotation", data_dir / "annotation.json"))
    output_dir = Path(cfg.get("output_dir", OUTPUT_ROOT / "vja" / cfg.get("experiment", "attack")))
    output_dir.mkdir(parents=True, exist_ok=True)
    h = cfg.get("hparams", {})
    prompt_field = h.get("prompt_field", "question")
    safe = bool(h.get("safe", False))
    max_samples = cfg.get("max_samples")
    device = "cuda" if torch.cuda.is_available() else "cpu"

    with open(ann_path, "r", encoding="utf-8") as handle:
        items = json.load(handle)
    if max_samples:
        items = items[: int(max_samples)]

    dtype = torch.bfloat16
    if safe:
        text_encoder = AutoModelForImageTextToText.from_pretrained(
            h.get("safety_model", "Qwen/Qwen2.5-VL-7B-Instruct"),
            dtype=dtype,
            attn_implementation=h.get("attn_implementation", "flash_attention_2"),
            device_map="auto",
        )
        pipeline = QwenImageEditSafePipeline.from_pretrained(
            h.get("base_model", "Qwen/Qwen-Image-Edit"),
            torch_dtype=dtype,
            text_encoder=text_encoder,
        )
    else:
        pipeline = QwenImageEditPlusPipeline.from_pretrained(
            h.get("base_model", "Qwen/Qwen-Image-Edit"),
            torch_dtype=dtype,
        )
    if h.get("cpu_offload"):
        pipeline.enable_model_cpu_offload()
    else:
        pipeline.to(device)

    results = []
    for item in items:
        image_path = _resolve_image(data_dir, item)
        prompt = item.get(prompt_field) or item.get("question")
        out_file = output_dir / f"{int(item['image_id']):04d}.png"
        record = {
            "image_id": item.get("image_id"),
            "category": item.get("category"),
            "prompt_field": prompt_field,
            "blocked": False,
            "error": None,
            "output": str(out_file),
        }
        try:
            image = Image.open(image_path).convert("RGB")
            output = pipeline(
                image=image,
                prompt=prompt,
                generator=torch.manual_seed(int(h.get("seed", 0))),
                true_cfg_scale=float(h.get("true_cfg_scale", 4.0)),
                negative_prompt=h.get("negative_prompt", " "),
                num_inference_steps=int(h.get("num_inference_steps", 40)),
            )
            output.images[0].save(out_file)
        except SafetyError as exc:
            record["blocked"] = True
            record["error"] = getattr(exc, "reason", str(exc))
        except Exception as exc:
            record["error"] = repr(exc)
        results.append(record)
        print(f"[vja] {item.get('image_id')} blocked={record['blocked']} err={record['error']}")

    with open(output_dir / "results.json", "w", encoding="utf-8") as handle:
        json.dump(results, handle, ensure_ascii=False, indent=2)
    n_ok = sum(1 for r in results if r["error"] is None)
    n_block = sum(1 for r in results if r["blocked"])
    print(f"[vja] done {n_ok}/{len(results)} saved, {n_block} blocked by introspective defense")
