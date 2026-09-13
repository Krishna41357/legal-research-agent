import sys
from pathlib import Path

# Add app/ to path so sibling packages (e.g. db) are importable
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from pdf_parser import extract_text_from_pdf
from text_cleaner import clean_text
from chunker import chunk_by_paragraph
from document_builder import create_documents
from embeddings import create_document_embeddings
from db.vector_store import store_documents


PROJECT_ROOT = Path(__file__).resolve().parents[2]

pdf_path = PROJECT_ROOT / "data" / "indian-constitution.txt.pdf"

text = extract_text_from_pdf(str(pdf_path))

cleaned_text = clean_text(text)

chunks = chunk_by_paragraph(cleaned_text)

documents = create_documents(chunks)

embeddings = create_document_embeddings(documents)

store_documents(documents, embeddings)

print(f"Stored {len(documents)} chunks successfully.")