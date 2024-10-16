import os
from .embedding_utils import generate_embedding_batch, load_model, save_embeddings
from .text_processing import preprocess_book_text
from backend.config import EMBEDDING_PATH

def upload_and_process_book(file_name, book_in_text = None, book_path = None):
    """
    Upload and process a book text file

    Parameters:
    book_path (str): Path to the book text file

    Returns:
    str: Book text
    list: List of sentences
    np.ndarray: Embedding matrix
    """
    
    if book_in_text:
        book_text = book_in_text
    elif book_path:    
        with open(book_path, 'r', encoding='utf-8') as f:
            book_text = f.read()
    
    sentence_list = preprocess_book_text(book_text)
    
    model = load_model()
    file_name = file_name.split('.')[0]
    embedding_matrix = generate_embedding_batch(sentence_list, model)
    EMBEDDING_PATH_NEW = os.path.join(EMBEDDING_PATH, file_name + '_' + 'embedding' + '.pkl')
    SENTENCE_LIST_PATH = os.path.join(EMBEDDING_PATH, file_name + '_' + 'sentence_list' + '.pkl')
    save_embeddings(embedding_matrix, sentence_list, EMBEDDING_PATH_NEW, SENTENCE_LIST_PATH)

    return book_text, sentence_list, embedding_matrix
