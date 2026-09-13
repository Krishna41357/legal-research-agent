# pyrefly: ignore [missing-import]
import fitz

def extract_text_from_pdf(pdf_path:str):
    document = fitz.open(pdf_path)
    pages = []

    for page in document:
        pages.append(page.get_text())
    
    document.close()
    return "\n".join(pages)


