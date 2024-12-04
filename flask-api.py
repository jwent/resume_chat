from flask import Flask, request, jsonify
import os
import openai

# Initialize Flask app
app = Flask(__name__)

# Set your OpenAI API key here
# Retrieve API key from environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

if not openai.api_key:
    raise ValueError("API key not found. Set the 'OPENAI_API_KEY' environment variable.")


def load_resume(file_path):
    """Load resume from a file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def ask_question(resume_text, question):
    """Use ChatGPT to answer a question about the resume."""
    prompt = f"Resume: {resume_text}\n\nQuestion: {question}\n\nAnswer:"

    completion = openai.ChatCompletion.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant that extracts information from resumes."},
            {"role": "user", "content": prompt}
        ],
        model="gpt-4"
    )
    return completion.choices[0].message.content.strip()

# Load the resume once to keep it ready for API calls
resume_text = load_resume('resume.txt')

@app.route('/ask', methods=['POST'])
def ask():
    """API endpoint to ask questions about the resume."""
    data = request.json
    question = data.get('question')
    
    if not question:
        return jsonify({'error': 'Please provide a question.'}), 400

    try:
        answer = ask_question(resume_text, question)
        return jsonify({'question': question, 'answer': answer})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
