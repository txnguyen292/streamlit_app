from pathlib import Path

file_dir = Path(__file__).resolve().parent

class CONFIG:
    data = file_dir / "data"
    models = file_dir / "models"
    imgs = file_dir / "imgs"

if __name__ == "__main__":
    pass