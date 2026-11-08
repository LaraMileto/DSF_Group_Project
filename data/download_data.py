
from pathlib import Path
from huggingface_hub import hf_hub_download

# Project directory
project_dir = Path(__file__).resolve().parent.parent

# Dataset folder
data_dir = project_dir / "data" / "raw"
data_dir.mkdir(parents=True, exist_ok=True)

# Hugging Face dataset repository
repo_id = "THUlab/freshretailnet_50k"

# Download the original training and evaluation files
files = [
    "freshretailnet_50k_train.tsfile",
    "freshretailnet_50k_eval.tsfile"
]

for filename in files:
    print(f"Downloading {filename}...")

    path = hf_hub_download(
        repo_id=repo_id,
        filename=filename,
        repo_type="dataset",
        local_dir=data_dir
    )

    print(f"Saved to: {path}")

print("Dataset download completed!")
