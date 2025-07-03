# rag.py
import faiss
import numpy as np

def build_faiss_index(embeddings):
    dimension = len(embeddings[0])
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings).astype("float32"))
    return index

def get_top_k_chunks(query_embedding, index, chunks, k=3):
    D, I = index.search(np.array([query_embedding]).astype("float32"), k)
    return [chunks[i] for i in I[0]]
def build_prompt(chunks, query):
    return "Use the following context:\n\n" + "\n".join(chunks) + f"\n\nQ: {query}\nA:"