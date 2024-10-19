import requests

# URL to which you want to send the POST request
url = "http://localhost:5000/similar-sentences"

# Data to be sent in the POST request
data = {
    "sentence": """'And I know,' said Bob, 'I know, my dears, that when we recollect how
patient and how mild he was; although he was a little, little child; we
shall not quarrel easily among ourselves, and forget poor Tiny Tim in
doing it.'""",
    "title": "Christmas Carol",
}

# Make the POST request
response = requests.post(url, json=data)

# Check the response
if response.status_code == 200:
    print("Success:", response.json())
else:
    print("Failed:", response.status_code, response.text)
