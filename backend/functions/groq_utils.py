from groq import Groq
import os
from .text_processing import get_context

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

context = get_context()

def get_groq_summary(similar_sentences, highlight, title):
    """
    Get a summary of the highlighted text based on similar sentences

    """
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": f"""
                    Act as an E-Reader assistant. I will give you a text from a book {title} that I am reading. I would
                    also provide you with similar sentences from the book as a list of strings. You need to use those
                    sentences and provide me more context into the highlited text. Use the Entity Context that is provided to build
                    the output. Look into who the people are, from the Entity Context and mention who the people are, and generate the overall context based on that.
                    The output should have the overall context directly. Make sure to keep the overall context relevant to the highlighted text.
                    Also make sure to keep the overall context short and concise. Make sure to keep the english simple and not advanced.

                    Give insight directly, don't mention about the highlighted text or the similar sentences. 
                    Just give me the final context.
                                """,
                                },
                                {
                                    "role": "user",
                                    "content": f"""
                    Highlighted Text: {highlight}
                    Similar Sentences: {similar_sentences}
                    Entity Context: {context}
                    Explain.
                """,
            },
        ],
        model="llama3-8b-8192",
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        stop=None,
        stream=False,
    )
    return chat_completion.choices[0].message.content
