import re

def preprocess_book_text(book_text):
    """
    Preprocess book text by removing newlines and splitting into sentences

    Parameters:
    book_text (str): Text of a book
    
    Returns:
    list: List of sentences
    """
    book_text = book_text.replace('\n', ' ').strip()
    
    # Split text into sentences using basic punctuation rules
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', book_text)
    return sentences
