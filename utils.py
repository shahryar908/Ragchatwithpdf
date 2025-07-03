import requests
import json
def get_ollama_embedding(text,model="nomic-embed-text"):
    url="http://localhost:11434/api/embeddings"
    payload={
        "model":model,
        "prompt":text
    }
    response=requests.post(url,json=payload)
    return response.json()["embedding"]
def get_ollama_answer(prompt, model="deepseek-r1:1.5b"):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": model, "prompt": prompt, "stream": True},
        stream=True
    )
    
    full_response = ""
    for chunk in response.iter_lines():
        if chunk:
            try:
                part = json.loads(chunk.decode("utf-8"))  # ← Replace eval() with this
                full_response += part["response"]
            except Exception as e:
                print("❌ Error decoding chunk:", e)            
    return full_response