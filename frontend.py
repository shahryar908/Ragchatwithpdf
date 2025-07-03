# app.py

import streamlit as st
from loadpdf import extract_text
from embedding import split_text_into_chunks, embed_chunks
from utils import get_ollama_embedding, get_ollama_answer
from generating import build_faiss_index, get_top_k_chunks, build_prompt

st.set_page_config(page_title="Talk with your PDF", page_icon="📚")
st.title("📚 Talk with your PDF")

# Initialize session state
if "index" not in st.session_state:
    st.session_state.index = None
if "chunks" not in st.session_state:
    st.session_state.chunks = None
if "text" not in st.session_state:
    st.session_state.text = None

# Upload PDF
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file and st.session_state.index is None:
    with st.spinner("Processing your document..."):
        # Extract text
        text = extract_text(uploaded_file)
        st.session_state.text = text

        # Split + embed
        chunks = split_text_into_chunks(text)
        embeddings = embed_chunks(chunks)

        # Build FAISS index
        index = build_faiss_index(embeddings)

        # Store in session
        st.session_state.index = index
        st.session_state.chunks = chunks

    st.success("Your PDF is ready for Q&A!")

# UI for asking questions
if st.session_state.index and st.session_state.chunks:
    query = st.text_input("💬 Ask a question about your PDF")

    if query:
        with st.spinner("Thinking..."):
            query_embedding = get_ollama_embedding(query)
            top_chunks = get_top_k_chunks(query_embedding, st.session_state.index, st.session_state.chunks)
            prompt = build_prompt(top_chunks, query)
            answer = get_ollama_answer(prompt)

        st.markdown(f"### 🧠 Answer:\n{answer}")
