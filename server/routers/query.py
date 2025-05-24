from fastapi import APIRouter, Request
from services.vector_store import get_vector_store
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
router = APIRouter()

@router.post('/query')
async def query_document(request: Request):
    body = await request.json()
    question = body.get("question")

    vector_store = get_vector_store()
    
    retriever = vector_store.as_retriever(search_kwargs={'k': 3})

    qa = RetrievalQA.from_chain_type(
        llm=ChatOpenAI(temperature=0),
        chai_type="stuff",
        retriever=retriever,
        return_source_document=True
    )

    result = qa(question)

    return {
        "question": question,
        "answer": result["result"],
        "source_documents": [doc.metadata for doc in result["source_documents"]]
    }
