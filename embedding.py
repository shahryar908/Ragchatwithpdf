# embedding.py
from utils import get_ollama_embedding

def split_text_into_chunks(text, chunk_size=300):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

def embed_chunks(chunks):
    return [get_ollama_embedding(chunk) for chunk in chunks]
