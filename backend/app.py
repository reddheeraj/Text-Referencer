from flask import Flask, request, jsonify
from flask_cors import CORS
from backend.functions.similarity_search import find_similar_sentences_cosine
from backend.functions.storage_manager import upload_and_process_book

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing (allow frontend to call APIs)

# Global variables to store embeddings and sentence list
embedding_matrix = None
sentence_list = None


@app.route("/upload-book", methods=["POST"])
def upload_book():
    """API to handle book upload and generate embeddings."""
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    file_name = file.filename
    book_text = file.read().decode("utf-8")

    global sentence_list, embedding_matrix

    book_text, sentence_list, embedding_matrix = upload_and_process_book(
        file_name=file_name, book_in_text=book_text
    )
    return (
        jsonify(
            {
                "message": "Book uploaded and processed",
                "num_sentences": len(sentence_list),
                "book_text": book_text,
            }
        ),
        200,
    )


@app.route("/similar-sentences", methods=["POST"])
def similar_sentences():
    """API to handle requests for finding similar sentences."""
    data = request.json
    sentence = data.get("sentence")
    title = data.get("title")
    if not sentence:
        return jsonify({"error": "No sentence provided"}), 400
    # Ensure the book has been uploaded
    if embedding_matrix is None or sentence_list is None:
        return jsonify({"error": "No book uploaded"}), 400

    # Perform the cosine similarity search

    similar = find_similar_sentences_cosine(
        sentence, title, sentence_list, embedding_matrix
    )
    return jsonify({"similar_sentences": similar}), 200


if __name__ == "__main__":
    app.run(debug=True, port=5000)
