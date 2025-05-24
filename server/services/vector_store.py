import os
from dotenv import load_dotenv
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

load_dotenv()

embedding_model = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
PERSIST_DIR = "vector_db/"


def store_chunks(chunks, doc_id):

    from langchain.schema import Document

    documents = [
        Document(page_content=chunk, metadata={"source": doc_id})
        for chunk in chunks
    ]

    db = Chroma.from_documents(documents, embedding=embedding_model, persist_directory=PERSIST_DIR)
    db.persist()

    return f"{len(chunks)} chunks stored in vector db for {doc_id}"

def get_vector_store():
    return Chroma(embedding_function=embedding_model, persist_directory=PERSIST_DIR)