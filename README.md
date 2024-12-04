# OpenAI Career Assistant

This project is an **OpenAI-powered app** designed to answer questions about your career based on the information provided in your resume. It's a personalized and interactive tool to help you showcase your professional journey, skills, and achievements in a conversational format.

---

## Features

- **Dynamic Question-Answering**: Users can ask questions about their career, such as:
  - "What are my top skills?"
  - "What accomplishments have I achieved?"
  - "What industries have I worked in?"
- **Resume Parsing**: Automatically extracts key information from your uploaded resume.
- **Custom Responses**: Provides detailed, conversational answers tailored to your career.

---

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/openai-career-assistant.git
   cd openai-career-assistant
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up API Key**
   - Create a `.env` file in the root directory.
   - Add your OpenAI API key:
     ```plaintext
     OPENAI_API_KEY=your_openai_api_key
     ```

---

## Usage

1. **Start the App**
   ```bash
   python app.py
   ```

2. **Upload Your Resume**
   - Use the web interface or terminal prompt to upload your resume file (`.pdf` or `.docx`).

3. **Ask Questions**
   - Start asking questions about your career directly in the app interface.

---

## Example

**Input**:  
"Can you summarize my work experience?"

**Output**:  
"You have over 7 years of experience in software development, specializing in full-stack engineering. Your most recent role was at XYZ Corp, where you led a team of developers to build scalable e-commerce platforms."

---

## Technology Stack

- **Backend**: Python, Flask/FastAPI
- **AI Engine**: OpenAI GPT API
- **Resume Parsing**: `pdfminer`/`docx`
- **Frontend**: HTML/CSS or CLI-based UI

---

## Contributing

We welcome contributions to improve the app! Please open an issue or submit a pull request to the repository.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Future Enhancements

- Multi-language support for answering questions.
- Integration with LinkedIn for real-time profile updates.
- Advanced analytics on career trends and skill gaps.

---

Happy exploring your career insights! 🚀