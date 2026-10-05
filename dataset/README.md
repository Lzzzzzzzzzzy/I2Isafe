# I2Isafe datasets

| Dir | Paper | Status |
|---|---|---|
| `AdvI2I/` | AdvI2I | Extracted from official `dataset.tar.gz` (395 images, 396 clothes masks, nudity/violence prompts) |
| `IESBench/` | VJA | 1054 images + `annotation.json` |
| `ColJailBreak/` | ColJailBreak | I2P-derived 105 prompts (paper Sec 5.1), SAM ViT-H. UnsafeEdit (100) was not released by the authors |
| `MFJ/JBB-Behaviors/` | MFJ | JailbreakBench harmful/benign 100+100. `javirandor/jbb-chameleon7b` is used at attack time if HF is reachable |
| `MMA-Diffusion/` | MMA-Diffusion | **Gated** on Hugging Face — request access then re-run `python scripts/download_datasets.py` |
| `MFJ/` MIMICIT | MFJ shortcut training | **Gated** (`pufanyi/MIMICIT`) — the official trainer streams it if you have access |

After Hugging Face auth (`huggingface-cli login`) and access approval:

```bash
export HF_ENDPOINT=https://hf-mirror.com   # or https://huggingface.co
python scripts/download_datasets.py
```
