from fastapi import FastAPI, HTTPException
from app.ingest import process_documents
from app.embeddings import generate_embeddings
from app.store import save_embeddings
from app.retrieval import retrieve
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "RAG API running"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/ingest")
def ingest_documents():
    chunks = process_documents("data")

    if not chunks:
        raise HTTPException(status_code=400, detail="No documents found in data folder")

    embedded_chunks = generate_embeddings(chunks)
    save_embeddings(embedded_chunks, "vector_store/data.json")

    return {
        "message": "Documents ingested successfully",
        "chunks_stored": len(embedded_chunks)
    }


@app.get("/query")
def query_rag(query: str, top_k: int = 3):
    if top_k < 1:
        raise HTTPException(status_code=400, detail="top_k must be greater than 0")

    results = retrieve(
        query=query,
        file_path="vector_store/data.json",
        top_k=top_k
    )

    return {
        "query": query,
        "results": results
    }