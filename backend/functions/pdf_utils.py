import re
import PyPDF2


def get_book_text(file):

    filename = file.filename
    if not filename.endswith(".pdf"):
        return file.read().decode("utf-8")
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:  # Check if text extraction was successful
            # Replace multiple tabs with a single space
            page_text = re.sub(r"\t+", " ", page_text)
            # Condense multiple spaces (including any new spaces created) to a single space
            page_text = re.sub(r"\s+", " ", page_text)
            text += page_text + "\n"
    return text.strip()
