from __future__ import annotations

import os


def set_offline_logging() -> None:
    os.environ.setdefault("WANDB_MODE", "offline")
    os.environ.setdefault("WANDB_DISABLED", "true")
    os.environ.setdefault("HF_HUB_DISABLE_TELEMETRY", "1")
