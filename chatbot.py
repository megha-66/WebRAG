import os

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_ollama import ChatOllama
from config import URLS, EMBEDDING_MODEL, DB_PATH

from dotenv import load_dotenv

load_dotenv()

os.environ["USER_AGENT"] = "WebRAG"

embeddings = HuggingFaceEmbeddings(
    model_name=EMBEDDING_MODEL
)

print("Loading Chroma database...")

db = Chroma(
    persist_directory=DB_PATH,
    embedding_function=embeddings
)

print("Database collection count: ",db._collection.count())

retriever = db.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 3}
)

llm = ChatOllama(
    model="llama3.2:1b",
    temperature=0.3
)

print("\nRAG Chatbot Ready!")
print("Type 'exit' to quit.\n")

while True:

    question = input("You: ")

    if question.lower() in ["exit", "quit"]:
        break

    docs = retriever.invoke(question)
    
    print(f"\nRetrieved {len(docs)} documents\n")

    for i, doc in enumerate(docs):
        print("=" * 80)
        print(f"Document {i+1}")
        print(doc.page_content)
    print("-"*80)

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )
    
    print("-"*80)
    print("\nContext passed to LLM:\n")
    print(context)
    print("-"*80)

    prompt = f"""
You are a helpful AI assistant.

Answer the user's question using the context below.

If the context contains the information, explain it clearly in your own words.

If the answer is not present, reply:

"I don't know based on the supplied documents."

Context:
{context}

Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)
    
    print("-"*80)
    print("\nAssistant:\n")
    print(response.content)
    print("-" * 80)
