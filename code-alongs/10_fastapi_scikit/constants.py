from pathlib import Path

MODELS_PATH = Path(__file__).parent / "models"
DATA_PATH = Path(__file__).parents[2] / "data"
ASSETS_PATH = Path(__file__).parents[2] / "assets"


# dependencies (uv pip install):
# pandas ipykernel seaborn scikit-learn fastapi uvicorn

print(MODELS_PATH.resolve())
print(DATA_PATH.resolve())
print(ASSETS_PATH.resolve())