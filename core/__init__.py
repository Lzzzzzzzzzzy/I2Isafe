"""I2Isafe core: paths, configs, and method dispatch."""

from .paths import DATASET_ROOT, I2I_ROOT, I2ISAFE_ROOT, OUTPUT_ROOT
from .config import load_config, resolve_config
from .runner import set_offline_logging
from .registry import get_adapter

__all__ = [
    "I2ISAFE_ROOT",
    "I2I_ROOT",
    "DATASET_ROOT",
    "OUTPUT_ROOT",
    "load_config",
    "resolve_config",
    "set_offline_logging",
    "get_adapter",
]
