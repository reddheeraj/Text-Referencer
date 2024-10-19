from groq import Groq

client = Groq(api_key="<Enter Groq API Key>")


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
also provide you with similar sentences from the book as a list of strings. You neex to use the context of those
sentences and provide me more insight into the highlited text. The output should have the insight directly.

Give insight directly, don't mention about the highlighted text or the similar sentences. Just give me the insight.
            """,
            },
            {
                "role": "user",
                "content": f"""
Highlighted Text: {highlight}
Similar Sentences: {similar_sentences}
Explain
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
