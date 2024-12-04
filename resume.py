import os
import openai

# Set your OpenAI API key here
# Retrieve API key from environment variable
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
        model="gpt-4o-mini",
    )
    # var_dump(completion)
    return completion.choices[0].message.content
    # return response['choices'][0]['message']['content'].strip()
    return

def var_dump(var):
    print(f'Type: {type(var)}')
    print(f'Value: {var}')

def main():
    resume_file_path = 'resume.txt'  # Path to the resume file
    resume_text = load_resume(resume_file_path)
    
    while True:
        '''question = input("Enter your question about the resume (or type 'exit' to quit): ")'''
        question = "How many years of C# does Jeremy have ?"
        if question.lower() == 'exit':
            break
        
        answer = ask_question(resume_text, question)
        print("Answer:", answer)

if __name__ == "__main__":
    main()
