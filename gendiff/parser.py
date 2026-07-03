import json
import yaml
from pathlib import Path


def parse_file(file_path):
    ext = Path(file_path).suffix.lower()

    with open(file_path, "r", encoding="utf-8") as file:
        if ext == ".json":
            return json.load(file)
        elif ext in [".yaml", ".yml"]:
            return yaml.safe_load(file)
        else:
            raise ValueError(f"Unsupported file extension: {ext}")
