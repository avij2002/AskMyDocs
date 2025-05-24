from PyPDF2 import PdfReader

def parse_pdf(file_path):
    text = ""
    with open(file_path, "rb") as file:
        reader = PdfReader(file)
        # loop through each page
        for page in reader.pages:
            text += page.extract_text() or ""

    return text