from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def generate_embeddings(chunks):
    embedded_chunks = []

    for chunk in chunks:
        embedding = model.encode(chunk["text"]).tolist()

        embedded_chunks.append({
            "text": chunk["text"],
            "source": chunk["source"],
            "embedding": embedding
        })

    return embedded_chunks