from __future__ import annotations

from pathlib import Path

_WORK = Path(".")


def set_work_path(path: str | Path) -> Path:
    global _WORK
    _WORK = Path(path)
    _WORK.mkdir(parents=True, exist_ok=True)
    (_WORK / "steer_vec").mkdir(exist_ok=True)
    (_WORK / "hf_results").mkdir(exist_ok=True)
    return _WORK


def work_dir() -> str:
    return str(_WORK) + "/"
