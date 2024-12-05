import json
import requests

def lambda_handler(event, context):
    url = "https://jsonplaceholder.typicode.com/posts/1"  # Example API
    response = requests.get(url)
    return {
        "statusCode": 200,
        "body": json.dumps(response.json())
    }
