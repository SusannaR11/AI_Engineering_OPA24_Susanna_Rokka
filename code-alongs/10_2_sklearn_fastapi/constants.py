from pathlib import Path

MODELS_PATH = Path(__file__).parent / "models"
DATA_PATH = Path(__file__).parents[2] / "data"

print(MODELS_PATH)
print(DATA_PATH)