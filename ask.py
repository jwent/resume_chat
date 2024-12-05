import requests

url = "http://localhost:5000/ask"
data = {"question": "How many years of C# does Jeremy have?"}

response = requests.post(url, json=data)
print(response.json())
