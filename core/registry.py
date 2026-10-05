from __future__ import annotations

import importlib
from typing import Any, Callable

_MODULE_BY_METHOD = {
    "advi2i": "attacks.advi2i",
    "coljailbreak": "attacks.coljailbreak",
    "mma_diffusion": "attacks.mma_diffusion",
    "mma-diffusion": "attacks.mma_diffusion",
    "mfj": "attacks.mfj",
    "multimodal-fusion-jailbreaks": "attacks.mfj",
    "vja": "attacks.vja",
}


def get_adapter(method: str) -> Callable[[dict[str, Any]], None]:
    key = method.strip().lower()
    if key not in _MODULE_BY_METHOD:
        raise KeyError(
            f"Unknown method {method!r}. Choose from: advi2i, coljailbreak, mma_diffusion, mfj, vja"
        )
    module = importlib.import_module(_MODULE_BY_METHOD[key])
    return module.run
