# RAG desde cero con FastAPI

Proyecto de Retrieval-Augmented Generation (RAG) construido desde cero en Python, sin frameworks de abstracción, con el objetivo de mostrar cómo funciona internamente un sistema de recuperación semántica. Incluye backend con FastAPI, generación de embeddings, persistencia local y un frontend simple tipo chat.

---

## Qué hace

- Lee documentos `.txt`
- Divide el texto en chunks
- Genera embeddings con un modelo preentrenado
- Guarda los vectores en disco (JSON)
- Permite hacer consultas semánticas
- Devuelve los chunks más relevantes (top-k)
- Interfaz web simple para interactuar

---

##  Cómo funciona

1. **Ingesta**
   - Lee archivos desde `data/`
   - Divide el texto en chunks de tamaño fijo
   - Ajusta cortes para no romper palabras

2. **Embeddings**
   - Usa `sentence-transformers` (`all-MiniLM-L6-v2`)
   - Convierte texto en vectores numéricos

3. **Almacenamiento**
   - Guarda embeddings en `vector_store/data.json`

4. **Retrieval**
   - Convierte la query en embedding
   - Calcula similitud (cosine similarity)
   - Ordena resultados y devuelve los más relevantes

---

## Instalación y uso

```bash
pip install -r requirements.txt
uvicorn main:app --reload

1. Agregar archivos .txt en la carpeta data/
2. Ingestar documentos desde Swagger: POST /ingest
3. Consultar: GET /query?query=tu_pregunta&top_k=3

## Nota

El archivo `vector_store/data.json` no se incluye en el repositorio.
Para generar los embeddings, ejecutar el endpoint `/ingest`.

## Frontend
1. cd frontend
2. python -m http.server 5500
3. Abrir en el navegador: http://127.0.0.1:5500
4. Interfaz tipo chat que consulta la API y muestra los resultados.