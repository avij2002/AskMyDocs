from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_text(text, chunk_size, chunk_overlap):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["/n/n", "/n", ".", " ", ""]
    )
    return splitter.split_text(text)