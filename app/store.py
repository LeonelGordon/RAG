import json


def save_embeddings(data, file_path):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_embeddings(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data