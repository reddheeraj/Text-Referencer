import boto3
import json

bedrock = boto3.client(service_name="bedrock-runtime", region_name="us-west-2")


def get_bedrock_summary(similar_sentences, highlight, title, context):
    # Create the Bedrock client

    # Prepare the input for the model
    input_data = {
        "modelId": "meta.llama3-70b-instruct-v1:0",
        "contentType": "application/json",
        "accept": "*/*",
        "body": json.dumps(
            {
                "prompt": f"""
Act as an E-Reader assistant. I will give you a text from a book {title} that I am reading. I would
also provide you with similar sentences from the book as a list of strings. You need to use those
sentences and provide me more context into the highlited text. The output should have the context directly.

Highlighted Text: {highlight}
Similar Sentences: {similar_sentences}
Entity Context: {context}

Give insight directly, don't mention about the highlighted text or the similar sentences. Just give me the context.
            """,
            }
        ),
    }

    response = bedrock.invoke_model(**input_data)
    output = json.loads(response["body"].read())
    generated_text = output["generation"]
    return generated_text
