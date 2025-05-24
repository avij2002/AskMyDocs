import shutil
from fastapi import APIRouter, UploadFile, File
from services.parser import parse_pdf
from services.chunker import chunk_text
from services.vector_store import store_chunks

router = APIRouter()

@router.post('/upload')
async def upload(file: UploadFile = File(...)):

    save_path = f"public/data/{file.filename}"
    with open(save_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # parsing the file
    if(file.filename.endswith(".pdf")):
        # logic to parse file
        parsed_text = parse_pdf(save_path)
    else:
        return {"error": "Only Pdf files supported currently"}
    
    # chunking
    chunks = chunk_text(parsed_text, 500, 50)    

    # embedding generation
    store_chunks(chunks, file.filename)
    
    return {"filename": file.filename, "status": "parsed", "text": parsed_text[:500], "chunks": chunks}
    