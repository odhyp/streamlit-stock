import json


def read_json(filename: str):
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
