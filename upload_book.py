import requests

# URL to which you want to send the POST request
url = "http://127.0.0.1:5000/upload-book"

# Path to the file you want to send
file_path = "./ChristmasCarol.txt"

# Open the file in binary mode
with open(file_path, "rb") as file:
    # Create a dictionary for the file to be sent
    files = {"file": file}

    # Make the POST request
    response = requests.post(url, files=files)

# Check the response
if response.status_code == 200:
    print("File uploaded successfully:", response.json())
else:
    print("Failed to upload file:", response.status_code, response.text)
