import os
import json
import openai
from flask import Flask, request, jsonify
import boto3
from botocore.exceptions import ClientError

# Use this code snippet in your app.
# If you need more information about configurations
# or implementing the sample code, visit the AWS docs:
# https://aws.amazon.com/developer/language/python/


def get_secret():
    secret_name = "chatgpt-secrets"
    region_name = "us-east-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    secret = get_secret_value_response['SecretString']
    print(secret)

 # Your code goes here.

# Initialize Flask app
app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

def load_resume(file_path):
    """Load resume from a file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        resume_text = file.read()
    return resume_text

def ask_question(resume_text, question):
    """Use ChatGPT to answer a question about the resume."""
    prompt = f"Resume: {resume_text}\n\nQuestion: {question}\n\nAnswer:"
    completion = openai.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant that extracts information from resumes."},
            {"role": "user", "content": prompt}
        ],
        model="gpt-4",
    )
    return completion.choices[0].message.content.strip()

# Load the resume when the app starts
RESUME_FILE_PATH = 'resume.txt'
resume_text = load_resume(RESUME_FILE_PATH)

@app.route('/ask', methods=['POST'])
def ask():
    """
    API endpoint to answer questions about the resume.
    Accepts a JSON payload with the 'question' field.
    """
    try:
        data = request.get_json()
        if not data or 'question' not in data:
            return jsonify({"error": "Invalid input, 'question' field is required"}), 400

        question = data['question']
        answer = ask_question(resume_text, question)
        return jsonify({"answer": answer})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
