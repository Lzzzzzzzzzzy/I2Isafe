# I2Isafe attack taxonomy

Five papers are wrapped as methods. Original algorithms stay in their repos; I2Isafe only supplies configs, dataset paths, and launchers.

| Method | Surface | What is optimized / rewritten | Typical victim |
|---|---|---|---|
| AdvI2I | adversarial **image** | VAE/noise generator under \(\ell_p\) ball, steered to an NSFW concept vector | SD-Inpaint, InstructPix2Pix |
| MMA-Diffusion | **text** tokens + **image** pixels | GCG-style prompt search; \(\ell_2\) image PGD to fool the safety checker | SD-1.5-Inpaint |
| ColJailBreak | **prompt substitution** then **edit** | Replace unsafe word (\(\lvert S\rvert=10\)), generate a safe image, SAM-mask + inpaint the unsafe object | DALL·E / GPT-4 image |
| MFJ | continuous **pixels** through a tokenizer shortcut | Train embed/vocab shortcut on MIMICIT, then 500-step image GD on JailbreakBench | Chameleon-7B |
| VJA | **visual prompt** inside the image | Hide the instruction in-image (IESBench); optional introspective VLM defense | Qwen-Image-Edit |

## Shared evaluation axes

- **ASR**: whether the unsafe intent is realized (NudeNet / Q16 / JailbreakBench judge / IESBench guard bypass).
- **Utility / stealth**: CLIP similarity, \(\ell_p\) size, editing validity (VJA EV), high-risk ratio (VJA HRR).

## Method ids used by `scripts/run.py`

`advi2i` · `coljailbreak` · `mma_diffusion` · `mfj` · `vja`
