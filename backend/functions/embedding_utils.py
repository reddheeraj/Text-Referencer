from sentence_transformers import SentenceTransformer
import pickle
import os


def load_model(model_name="paraphrase-MiniLM-L6-v2"):
    """
    Load a SentenceTransformer model by name

    Parameters:
    model_name (str): Name of the SentenceTransformer model

    Returns:
    SentenceTransformer: SentenceTransformer model
    """
    return SentenceTransformer(model_name)


def generate_embedding_batch(sentences, model):
    """
    Generate embeddings for a list of sentences using a SentenceTransformer model

    Parameters:
    sentences (list): List of sentences
    model (SentenceTransformer): SentenceTransformer model

    Returns:
    np.ndarray: Embedding matrix
    """
    return model.encode(sentences, convert_to_tensor=True).cpu().numpy()


# Save embeddings and sentence list to file
def save_embeddings(
    embedding_matrix, sentence_list, embedding_path, sentence_list_path
):
    """
    Save embeddings and sentence list to file

    Parameters:
    embedding_matrix (np.ndarray): Embedding matrix
    sentence_list (list): List of sentences
    embedding_path (str): Path to save embedding matrix
    sentence_list_path (str): Path to save sentence list
    """
    # create path if it doesn't exist

    os.makedirs(os.path.dirname(embedding_path), exist_ok=True)
    os.makedirs(os.path.dirname(sentence_list_path), exist_ok=True)

    with open(embedding_path, "wb") as f:
        pickle.dump(embedding_matrix, f)
    with open(sentence_list_path, "wb") as f:
        pickle.dump(sentence_list, f)


# Load embeddings and sentence list from file
def load_embeddings(embedding_path, sentence_list_path):
    """
    Load embeddings and sentence list from file

    Parameters:
    embedding_path (str): Path to embedding matrix
    sentence_list_path (str): Path to sentence list

    Returns:
    np.ndarray: Embedding matrix
    list: List of sentences
    """
    with open(embedding_path, "rb") as f:
        embedding_matrix = pickle.load(f)
    with open(sentence_list_path, "rb") as f:
        sentence_list = pickle.load(f)
    return embedding_matrix, sentence_list
