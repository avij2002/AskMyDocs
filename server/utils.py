from PyPDF2 import PdfReader

def load_pdf_text(filePath):
    reader = PdfReader(filePath)
    raw_text = ""

    for page in reader.pages:
        if(page.extract.text()):
            raw_text += page.extract.text()
    return raw_text
