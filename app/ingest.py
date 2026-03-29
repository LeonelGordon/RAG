import os


def load_documents(folder_path: str):
    documents = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)

            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                documents.append({
                    "text": content,
                    "source": filename
                })

    return documents

def chunk_text(text: str, chunk_size: int = 300):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start = end
    return chunks

def process_documents(folder_path: str, chunk_size: int = 300):
    documentos = load_documents(folder_path)
    all_chunks = []

    for documento in documentos:
        chunks = chunk_text(documento["text"], chunk_size)
        for chunk in chunks:
            all_chunks.append({
            "text": chunk,
            "source": documento["source"]
        })

    return all_chunks