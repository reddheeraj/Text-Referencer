from sklearn.metrics.pairwise import cosine_similarity

from backend.functions.bedrock_utils import get_bedrock_summary
from backend.functions.groq_utils import get_groq_summary
from backend.functions.text_processing import get_context
from .embedding_utils import generate_embedding_batch
import numpy as np
from .embedding_utils import load_model

context = get_context()


def find_similar_sentences_cosine(
    query_text, title, sentence_list, embedding_matrix, k=10
):
    """
    Find the top k most similar sentences to a query sentence using cosine similarity

    Parameters:
    query_text (str): Query sentence
    sentence_list (list): List of sentences
    embedding_matrix (np.ndarray): Embedding matrix
    k (int): Number of similar sentences to return
    model (SentenceTransformer): SentenceTransformer model

    Returns:
    list: Top k most similar sentences
    """
    model = load_model()
    query_embedding = generate_embedding_batch([query_text], model)

    query_embedding = normalize_embeddings(query_embedding)
    embedding_matrix = normalize_embeddings(embedding_matrix)
    similarities = cosine_similarity(query_embedding, embedding_matrix)
    top_k_indices = np.argsort(similarities[0])[-k:][::-1]
    similar_sentences = [sentence_list[i] for i in top_k_indices]
    print("Similar Sentences:", similar_sentences)

    return get_bedrock_summary(similar_sentences, query_text, title, context)


# Function to normalize embeddings
def normalize_embeddings(embeddings):
    """
    Normalize embeddings to have unit norm

    Parameters:
    embeddings (np.ndarray): Embedding matrix

    Returns:
    np.ndarray: Normalized embeddings
    """
    norms = np.linalg.norm(embeddings, axis=1, keepdims=True)
    return embeddings / norms
