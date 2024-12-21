import streamlit as st
import google.generativeai as genai
import dotenv
import os
from zipfile import ZipFile
import requests
import io

# Load environment variables
dotenv.load_dotenv()

# Function to read ZIP file from URL
def read_zip(url: str) -> list:
    """Download and read ZIP file contents from a given URL."""
    response = requests.get(url)
    with ZipFile(io.BytesIO(response.content)) as zip_file:
        file_tree = []
        for file in zip_file.namelist():
            if file.endswith("/"):
                continue
            try:
                with zip_file.open(file, "r") as f:
                    contents = f.read().decode()
                    file_tree.append(f"\n---{file}---\n{contents}")
            except UnicodeDecodeError:
                pass  # Ignore files that can't be decoded
    return file_tree

# Streamlit application
def main():
    st.title("Git-Chat")

    # Input for GitHub repository URL
    repo_url = st.text_input("Enter the GitHub repository URL (e.g., 'https://github.com/username/repository'):")

    if repo_url and st.button("Fetch Repository"):
        with st.spinner("Fetching repository..."):
            try:
                # Extract the repo name from the URL
                repo_name = "/".join(repo_url.rstrip('/').split('/')[-2:])
                contents = read_zip(f"https://api.github.com/repos/{repo_name}/zipball")
                str_contents = "\n".join(contents)

                # Initialize the Generative AI model
                genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
                model = genai.GenerativeModel(
                    "gemini-1.5-flash",
                    system_instruction=f"""
                    You are a copilot who helps the user with code related questions.
                    The following is the full codebase that the user is working in:
                    {str_contents}
                    """,
                )
                st.session_state.chat = model.start_chat(history=[])
                st.session_state.repo_fetched = True
                st.success("Repository loaded successfully! You can now ask questions.")
            except Exception as e:
                st.error(f"Failed to fetch repository: {e}")

    # Chat functionality
    if "chat" in st.session_state:
        user_message = st.text_input("Enter your query:")

        if st.button("Submit") or st.session_state.get("history"):
            if user_message:
                response = st.session_state.chat.send_message(user_message, stream=True)
                response_text = "".join(chunk.text for chunk in response)
                if "history" not in st.session_state:
                    st.session_state.history = []
                st.session_state.history.append({"user": user_message, "bot": response_text})

            # Display conversation history
            for entry in st.session_state.history:
                st.write(f"**You**: {entry['user']}")
                st.write(f"**Bot**: {entry['bot']}")

        # Handle session reset (clear all queries and state)
        if st.button("Reset"):
            st.session_state.clear()  # Clear the entire session state
            st.experimental_rerun()  # Refresh the page to start fresh

if __name__ == "__main__":
    main()
