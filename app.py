import os
import google.generativeai as genai
import gradio as gr
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# System prompt for code generation
SYSTEM_PROMPT = """You are a helpful coding assistant that generates Python code snippets and templates.

When a user requests code:
1. Generate clean, well-commented Python code
2. Explain what the code does
3. Provide usage examples if relevant
4. Use markdown code blocks with ```python

Keep responses concise and focused on the code."""

# Initialize model
model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    generation_config={
        "temperature": 0.7,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 2048,
    }
)

def chat(message, history):
    """Process user message and return AI response"""

    # Build conversation context
    messages = []

    # Add system prompt
    messages.append({"role": "user", "parts": [SYSTEM_PROMPT]})
    messages.append({"role": "model", "parts": ["Understood. I'll help generate Python code snippets with clear explanations."]})

    # Add conversation history
    for user_msg, assistant_msg in history:
        messages.append({"role": "user", "parts": [user_msg]})
        messages.append({"role": "model", "parts": [assistant_msg]})

    # Add current message
    messages.append({"role": "user", "parts": [message]})

    # Generate response
    chat_session = model.start_chat(history=messages[:-1])
    response = chat_session.send_message(message)

    return response.text

# Create Gradio interface
demo = gr.ChatInterface(
    fn=chat,
    title="Python Code Snippet Generator",
    description="Ask me to generate Python code snippets, templates, or explain code concepts!",
    examples=[
        "Create a function to read a CSV file with pandas",
        "Show me how to make a REST API call with requests",
        "Generate a class for a simple to-do list manager",
        "How do I use list comprehensions?",
    ],
    theme=gr.themes.Soft(),
    retry_btn=None,
    undo_btn="Delete Previous",
    clear_btn="Clear Chat",
)

if __name__ == "__main__":
    demo.launch()
