This folder is filled by `scripts/download_datasets.py`.

The official MMA-Diffusion image/prompt benchmarks are gated:

- https://huggingface.co/datasets/YijunYang280/MMA_Diffusion_adv_images_benchmark
- https://huggingface.co/datasets/YijunYang280/MMA-Diffusion-NSFW-adv-prompts-benchmark

Request access, run `huggingface-cli login`, then re-run the download script. Expected layout:

```
MMA-Diffusion/
  mma_diffusion_images/   # *.png + *_mask.png from mma_diffusion_images.zip
  assets/                 # safety_checker.pt and related tensors
  adv_prompts.jsonl
```
