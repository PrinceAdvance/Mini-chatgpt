# Mini-chatgpt
A lightweight Streamlit app that connects to **Azure AI (LangChain integration)** and provides a simple chat interface using **GPT-4.1**.

---

## Features
- Streamlit-based user interface
- Uses LangChain’s `AzureAIChatCompletionsModel`
- Connects to GPT-4.1 for AI-powered responses
- Minimal setup, just run and chat

---

## Requirements
- Python 3.9+
- [Streamlit](https://streamlit.io)
- [LangChain Azure AI](https://python.langchain.com/)


## Project Setup

### 1. Create a virtual environment

```bash
python -m venv .venv
```

### 2. Activate the virtual environment

for macOS / Linux (bash or zsh)

```bash
source .venv/bin/activate
```

for Windows (PowerShell)

```powershell
.\.venv\Scripts\Activate.ps1
```

for Windows (cmd)

```cmd
.\.venv\Scripts\activate.bat
```

Your shell prompt should now show `(.venv)` to indicate the environment is active.

### 3. Install dependencies

```bash
pip install langchain-azure-ai streamlit
```

The Github credentials in the `chat.py` file are all the same. It will pick up your Github Token automatically. For more info on Github models look [here](https://github.com/marketplace/models).

## Run the app
You can run the app by running the following in the terminal:

```bash
streamlit run chat.py
```

# Took inspiration from @marlenezw
