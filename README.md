# 🧠 RAG PDF Chatbot with Ollama, FAISS & Streamlit

This is a beginner-friendly project that lets you **upload a PDF file and ask questions about its content** using a local LLM. It's built with:

* 🔍 **FAISS**: Fast vector search to retrieve relevant document chunks
* 🧠 **Ollama**: Runs LLMs locally (e.g. DeepSeek, LLaMA3, Mistral)
* 🖥️ **Streamlit**: Simple web app to ask questions and see results
* 📄 **PyMuPDF**: Extracts text from PDFs

---

## 🚀 What You Can Do

* Upload a PDF (e.g. human rights, laws, research papers)
* Ask a question like "What is Article 27 about?"
* Get the most relevant answer generated from the actual document

Everything runs **completely offline**. No internet is needed after setup.

---

## 🧰 Tech Stack

| Tool      | Purpose                                 |
| --------- | --------------------------------------- |
| Python    | Core language                           |
| PyMuPDF   | Extract text from uploaded PDF          |
| FAISS     | Search relevant chunks using embeddings |
| Ollama    | Generate embeddings + answers locally   |
| Streamlit | Simple, fast interactive web UI         |

---

## 🖥️ Setup Instructions

### 1. 📁 Clone the Repo

```bash
git clone https://github.com/yourusername/Ragchatwithpdf.git
cd Ragchatwithpdf
```

### 2. 🐍 Install Python Requirements

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install streamlit faiss-cpu pymupdf requests numpy
```

### 3. ⚙️ Install & Run Ollama

Download Ollama → [https://ollama.com/download](https://ollama.com/download)

Then pull and run models:

```bash
ollama run nomic-embed-text     # for embeddings
ollama run deepseek-r1:1.5b     # for answers (or use llama3)
```

Make sure these are running in the background.

---

## 📄 How It Works

### ➤ Step 1: Upload a PDF and Build Vector DB

Run the following to upload and embed your PDF


This will:

* Ask you to upload a `.pdf`
* Extract text from each page
* Split text into small overlapping chunks
* Create embeddings for each chunk using Ollama’s `nomic-embed-text`
* Save the data as `faiss_index.bin` and `chunks.pkl`

You only need to do this **once per document**.

### ➤ Step 2: Run the RAG Chatbot

Once the embeddings are saved, launch the chatbot:

```bash
streamlit run frontend.py
```

You can now:

* Type a question like: `What does the document say about education?`
* Get an answer generated from the most relevant chunks

---

## 📁 Project Structure

```
rag-pdf-chatbot/
├── generate.py         # Upload & embed PDF (creates DB)
├── rag.py              # Streamlit app for Q&A
├── faiss_index.bin     # FAISS vector index (auto-created)
├── chunks.pkl          # Embedded text chunks (auto-created)
├── requirements.txt    # Dependencies
├── README.md           # This file
└── data/               # PDF upload folder
```

---

## 💬 Example Use

```text
🧠 Question: What is Article 26?
✅ Retrieved Chunks: Text related to education rights
🗣 Answer: Everyone has the right to education. It shall be free at elementary levels...
```

---

## ⚙️ Customization Options

| Feature          | How to Change                                 |
| ---------------- | --------------------------------------------- |
| Chunk size       | Edit `chunk_text()` in `generate.py`          |
| Embedding model  | Change model name in `get_ollama_embedding()` |
| LLM model        | Change model in `get_ollama_answer()`         |
| Retrieved Chunks | Change `k` value in `get_top_k_chunks()`      |

---

## 💡 Ideas for Improvements

* Support for uploading **multiple PDFs**
* Option to **summarize documents**
* Use **LangChain** for more advanced workflows
* Add **chat memory** or history sidebar

---

## 🛡️ Why Use This Project?

* ✅ **Local & Private**: No API keys or internet needed
* 💼 **Great for Portfolio**: Showcase your knowledge of NLP, embeddings, and Streamlit
* 🔒 **Secure**: Perfect for legal, private, or confidential documents

---

## 🧠 Credits

* [Ollama](https://ollama.com)
* [FAISS](https://github.com/facebookresearch/faiss)
* [Streamlit](https://streamlit.io)
* [PyMuPDF](https://pymupdf.readthedocs.io)

---


## 📄 License

This project is open-source under the MIT License. You can use, modify, and share it freely.

---

## 🙋‍♂️ Need Help?

If you’re stuck, feel free to open an issue or connect with me!

---

Happy building! 🚀
