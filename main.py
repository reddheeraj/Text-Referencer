import streamlit as st
import pickle
from backend.functions.storage_manager import upload_and_process_book
from backend.functions.similarity_search import find_similar_sentences_cosine


st.title("Book Reference Tool")

st.subheader("Upload a book text file:")
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    with open('uploaded_book.txt', 'wb') as f:
        f.write(uploaded_file.getvalue())
    st.write("Book uploaded successfully!")

    book_text, sentence_list, embedding_matrix = upload_and_process_book(book_path='uploaded_book.txt')

    if book_text:
        query_sentence = st.text_input("Enter a sentence:")
        if query_sentence:
            similar_sentences = find_similar_sentences_cosine(query_sentence, sentence_list, embedding_matrix)
            # similar_sentences_indices = find_similar_sentences_cosine(query_sentence)
            # similar_sentences = [sentence_list[i] for i in similar_sentences_indices]

            st.write("Most similar sentences:")
            for idx, sentence in enumerate(similar_sentences):
                st.write(f"{idx + 1}. {sentence}")
