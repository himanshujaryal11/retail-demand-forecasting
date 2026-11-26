from pathlib import Path
import json
from src.model import train_model

def main():
    Path("artifacts").mkdir(exist_ok=True)
    metrics = train_model()
    print(json.dumps(metrics, indent=2))

if __name__ == "__main__":
    main()
