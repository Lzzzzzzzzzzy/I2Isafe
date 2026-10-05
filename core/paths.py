from pathlib import Path

I2ISAFE_ROOT = Path(__file__).resolve().parents[1]
I2I_ROOT = I2ISAFE_ROOT.parent
DATASET_ROOT = I2ISAFE_ROOT / "dataset"
OUTPUT_ROOT = I2ISAFE_ROOT / "outputs"
CONFIG_ROOT = I2ISAFE_ROOT / "configs"

REPOS = {
    "advi2i": I2I_ROOT / "AdvI2I",
    "coljailbreak": I2I_ROOT / "coljailbreak",
    "mma_diffusion": I2I_ROOT / "MMA-Diffusion",
    "mfj": I2I_ROOT / "multimodal-fusion-jailbreaks",
    "vja": I2I_ROOT / "VJA",
}

DATASET_DIRS = {
    "advi2i": DATASET_ROOT / "AdvI2I",
    "coljailbreak": DATASET_ROOT / "ColJailBreak",
    "mma_diffusion": DATASET_ROOT / "MMA-Diffusion",
    "mfj": DATASET_ROOT / "MFJ",
    "vja": DATASET_ROOT / "IESBench",
}
