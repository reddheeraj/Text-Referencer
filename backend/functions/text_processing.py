import re
import os
import json
from groq import Groq
from dotenv import load_dotenv
from ..config import EMBEDDING_PATH, output_json_path


load_dotenv()

llm = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

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

def get_file_name():
    try:
        with open(os.path.join(EMBEDDING_PATH, 'file_name.txt'), 'r') as f:
            file_name = f.read()
        return file_name
    except:
        pass
def get_context():
    try:
        file_name = get_file_name()
        with open(os.path.join(EMBEDDING_PATH, file_name, output_json_path), 'r') as f:
            data = json.load(f)
        return data
    except:
        pass

def run_processing_pipeline(book_text, output_folder, output_json_path):
    process_book(book_text, output_folder)
    merge_json_files(output_folder, output_json_path)

    with open(output_json_path, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
        merged_list = merge_entries(data)
    
    # clear the json file first
    open(output_json_path, 'w').close()

    with open(output_json_path, "w", encoding="utf-8") as output_file:
        json.dump(merged_list, output_file, ensure_ascii=False, indent=4)

def read_text_file(txt_path):
    with open(txt_path, "r", encoding="utf-8") as text_file:
        text = text_file.read()
    return text

def split_text(text, max_chunk_size=50000):
    chunks = []
    text_length = len(text)
    print("text_length = ", text_length)
    for i in range(0, text_length, max_chunk_size):
        chunk = text[i:i + max_chunk_size]
        chunks.append(chunk)
    print("len(chunks) = ", len(chunks))
    return chunks

def process_chunk(chunk):
    chat_completion = llm.chat.completions.create(

    messages=[
        {
            "role": "system",
            "content": """
            you are a helpful E-reader book assistant. You help people understand the content of the book.
            You are being given a text file which is a book. You will extract the entities from given text.
            You will extract only the entities and about that entity. An Entity is a person, place, or thing.
            """,
        },
        {
            "role": "user",
            "content": f"""
            You are being given a text file which is a book. Extract the people from given text.
            I want you to extract only the entity and about that entity. An Entity is a person, place, or thing.
            Please follow the below example. I want the output to be exactly followed. Do not include any other information. Just give
            the output as formatted below in the example. only give the list. do not give anything else before or after, just the list.

            Example:
            Input: some text
            Output: 
                [
                    {{
                        'Entity': 'Jinchul Woo',
                        'About': 'He was an A-rank hunter so powerful that, had his magic power evaluation been slightly higher, he would’ve been the second S-rank hunter to join the association after President Go. He had four years of practical experience under his belt and was a top-tier A-rank hunter.'
                    }},
                    {{
                        'Entity: 'President Go',
                        'About': 'He was the President of the Korean Hunter Association. He had highly valued Jinchul, who had elected to work for the association despite being courted by large guilds.'
                    }},
                    {{
                        'Entity': 'Kasaka's Fang',
                        'About': 'A dagger made out of the Snake Kasaka's tooth fangs.'
                    }}
                ]

            This is the book: {chunk}
            """,
        }
    ],

    model="llama-3.1-70b-versatile",
    temperature=0.5,
    max_tokens=1024,
    top_p=1,
    stop=None,
    stream=False,
    )
    result = chat_completion.choices[0].message.content
    # print("eval(result) = ", eval(result))
    return result

def process_book(text, output_folder):
    chunks = split_text(text)
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for i, chunk in enumerate(chunks):
        print(f"Processing chunk {i + 1} of {len(chunks)}...")
        result = process_chunk(chunk)
        
        json_file_path = os.path.join(output_folder, f"chunk_{i + 1}.json")
        
        with open(json_file_path, "w", encoding="utf-8") as json_file:
            result = result.strip()
            json.dump(result, json_file, ensure_ascii=False, indent=4)
    
    print(f"Processing complete. Each chunk's results saved as separate JSON files in {output_folder}")

def merge_json_files(input_folder, output_json_path):
    merged_list = []
    
    for file_name in os.listdir(input_folder):
        if file_name.endswith(".json"):
            file_path = os.path.join(input_folder, file_name)
            with open(file_path, "r", encoding="utf-8") as json_file:
                data = json.load(json_file)
                data = eval(data)
                merged_list.extend(data)  # Add the list from this file to the master list
    
    # Save the merged list as a single JSON file
    with open(output_json_path, "w", encoding="utf-8") as output_file:
        json.dump(merged_list, output_file, ensure_ascii=False, indent=4)
    
    print(f"All JSON files merged and saved to {output_json_path}")

def merge_entries(data):
    merged_dict = {}

    for entry in data:
        name = entry["Entity"]
        
        if name in merged_dict: 
            merged_dict[name]["About"] += f", {entry['About']}"
        else:
            merged_dict[name] = {
                "Entity": name,
                "About": entry["About"],
            }
    merged_list = list(merged_dict.values())
    return merged_list
