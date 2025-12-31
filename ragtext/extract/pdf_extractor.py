from __future__ import annotations
import os
import fitz
from ragtext.models import PageText

def extract_pdf_pages(pdf_path: str, doc_id: str | None = None) -> list[PageText]:
    """
    Extract raw text per PDF page. Keeps page boundaries for provenance.
    """
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(pdf_path)

    source_file = os.path.basename(pdf_path)
    doc_id = doc_id or os.path.splitext(source_file)[0]

    pages: list[PageText] = []
    with fitz.open(pdf_path) as doc:
        for i in range(len(doc)):
            page = doc.load_page(i)
            text = page.get_text("text") or ""
            pages.append(PageText(
                doc_id=doc_id,
                source_file=source_file,
                page_num=i + 1,
                text=text
            ))
    return pages
