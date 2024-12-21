# Git-Chat: Your GitHub Repository Code Assistant

Git-Chat is a Streamlit-based application that uses Google's Generative AI (Gemini) to provide intelligent assistance for GitHub repository codebases. Simply input a GitHub repository URL, and Git-Chat will fetch the code, analyze it, and provide answers to your queries.

## Features

- **Fetch GitHub Repositories**: Enter the repository URL, and Git-Chat downloads the repository's codebase as a ZIP file.
- **AI-Powered Chat Assistant**: Leverages Google's Generative AI to answer questions about the repository's code.
- **Interactive Chat**: Query the assistant for explanations, debugging help, or insights into the codebase.
- **Session Management**: Clear session state to reset the interaction.

---

## Installation

### Prerequisites
- Python 3.8 or later
- A valid API key for Google's Generative AI (Gemini)

### Setup

1. Clone this repository:
   ```bash
   git clone <repository_url>
   cd git-chat
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add your Gemini API key:
   ```plaintext
   GEMINI_API_KEY=your_api_key_here
   ```

---

## Usage

1. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

2. Open the application in your browser (usually at `http://localhost:8501`).

3. Enter a GitHub repository URL (e.g., `https://github.com/username/repository`) and click **Fetch Repository**.

4. Start asking questions about the codebase. For example:
   - "What does the `main.py` file do?"
   - "Can you explain the structure of this repository?"
   - "What are the potential bugs in the `utils.py` file?"

5. Reset the session if needed to start fresh.

---

## Project Structure

```
.
├── app.py             # Main Streamlit application
├── requirements.txt   # Python dependencies
├── .env.example       # Environment variable template
└── README.md          # Project documentation
```

---

## Technologies Used

- **Streamlit**: Frontend for interactive user input.
- **Google Generative AI (Gemini)**: AI model for generating code insights.
- **Python**: Core programming language.
- **Requests**: For handling HTTP requests.
- **dotenv**: For managing environment variables.
- **zipfile**: For handling repository ZIP files.

---

## Limitations

- The assistant might struggle with large or highly complex repositories.
- Only public repositories are supported.
- AI responses depend on the quality of the repository's structure and documentation.

---

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue for suggestions and improvements.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## Acknowledgements

- Powered by [Streamlit](https://streamlit.io/) and [Google Generative AI](https://cloud.google.com/ai).
- Inspired by the need for intelligent, AI-driven code assistance.

--- 
