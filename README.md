# agent_from_scratch_no_frameworks

A minimal chat-agent implemented from scratch using the OpenAI Python SDK. This repo contains a tiny interactive example (main.py) that keeps conversation history and sends it to the OpenAI Responses API.

## Features
- Minimal, dependency-light interactive chat loop
- Conversation history with system, user, and assistant roles
- Graceful exit using `exit` or `quit`

## Requirements
- Python 3.8+
- OpenAI Python SDK
- python-dotenv

## Installation
1. Clone the repo:
   git clone https://github.com/jomejia23/agent_from_scratch_no_frameworks.git
2. Create and activate a virtual environment (recommended):
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
3. Install dependencies:
   pip install openai python-dotenv

(Optionally add a requirements.txt with:
openai
python-dotenv
)

## Configuration
Create a `.env` file at the project root containing your OpenAI API key:

OPENAI_API_KEY=sk-...

main.py uses python-dotenv to load environment variables.

## Usage
Run the example:

python main.py

Type messages at the prompt. To quit, type `exit` or `quit`.

Example session:
You: Hello
Assistant: Hi! How can I help?

## How it works
- main.py loads environment variables and instantiates an OpenAI client.
- It maintains a `Messages` list with roles (`system`, `user`, `assistant`) and appends each user input and assistant reply.
- Each loop sends the full message history to `client.responses.create()` using the `gpt-4o` model and prints the assistant reply.

## Files
- main.py — Minimal interactive chat agent.
- README.md — This document.

## Suggested improvements
- Add error handling around the API call (network errors, rate limits).
- Limit conversation history or summarize older messages to avoid token overuse.
- Allow selecting different models via CLI or environment variables.
- Add a requirements.txt and simple tests.
- Persist conversation to a file for later replay or analysis.

## Troubleshooting
- Ensure OPENAI_API_KEY is set and valid.
- If you see import errors, verify dependencies are installed in the active environment.

## License
Add a license file (e.g., MIT) if you intend to open-source this repository.
