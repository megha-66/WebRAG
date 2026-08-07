# WebRAG: An Intelligent Website Question Answering System

- A lightweight <strong>Retrieval Augmented Generation (RAG)</strong> application. 
- Enables users to ask natural language questions about the provided website content. 
- The system extracts information from webpages, converts them into semantic vector embeddings, retrieves the most relevant context using <strong>ChromaDB</strong>, and generates accurate, context-aware responses using a locally hosted LLM through <strong>Ollama</strong>.

<p>Built with LangChain 1.x, ChromaDB, HuggingFace Embeddings, and Ollama. </p>

---
## Features 

- Retrieval Augmented Generation (RAG)
- Web page ingestion using WebBaseLoader
- Automatic Document chunking
- Semantic search with Chroma Vector Database
- Local inference using Ollama
- HuggingFace Sentence embeddings
- Modular project structure
- No cloud based LLM APIs required

---
## Tech Stack 

1. Python 3.10+
2. LangChain 1.x
3. ChromaDB
4. Hugging Face Embeddings (```BAAI/bge-base-en-v1.5```)
5. Ollama
6. Llama 3.2 (1B) (*or any compatible Ollama model*)

---
## Project Structure 

WebRAG/ \
│ \
├── ingest.py           # Builds the vector database \
├── chatbot.py          # Runs the chatbot \
├── chroma_db/          # Persistent Chroma database\
├── .env.example \
├── .gitignore \
├── requirements.txt \
└── README.md 

---
## Installation 

1. Clone the repository
```
git clone <repo-url>
cd WebRAG
```
2. Create a virtual environment
```
python3 -m venv rag 
source rag/bin/activate 
```
3. Install dependencies
```
pip install -r requirements. txt
```
4. Download and install Ollama from

5. Pull an LLM

   



