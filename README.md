# Python Code Snippet Generator

A minimal AI agent that generates Python code snippets using Google Gemini and Gradio.

## Features

- Chat-based interface for requesting code
- Conversation history maintained during session
- Syntax highlighting for generated code
- Explanations and usage examples

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Get a Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

3. Create a `.env` file:
```bash
cp .env.example .env
```

4. Add your API key to `.env`:
```
GEMINI_API_KEY=your_actual_api_key_here
```

## Usage

Run the app:
```bash
python app.py
```

The interface will open in your browser. Ask for Python code snippets like:
- "Create a function to sort a dictionary by values"
- "Show me how to connect to a SQLite database"
- "Generate a class for handling JSON files"

## Example Requests

- "Write a function to validate email addresses"
- "Create a decorator for timing function execution"
- "Show me how to use asyncio for concurrent tasks"
- "Generate code for reading environment variables"
