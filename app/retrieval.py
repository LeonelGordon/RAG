from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from app.store import load_embeddings


model = SentenceTransformer("all-MiniLM-L6-v2")


def retrieve(query: str, file_path: str, top_k: int = 3):
    stored_embeddings = load_embeddings(file_path)
    query_embedding = model.encode(query)

    results = []

    for item in stored_embeddings:
        score = cosine_similarity([query_embedding], [item["embedding"]])[0][0]

        results.append({
            "text": item["text"],
            "source": item["source"],
            "score": score
        })

    results.sort(key=lambda x: x["score"], reverse=True)

    return results[:top_k]