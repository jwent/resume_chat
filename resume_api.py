import os
import json
import openai
from flask import Flask, request, jsonify

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
