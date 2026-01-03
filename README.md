# Virtual Resume - AI Agent

An interactive AI-powered resume that acts as your personal representative, answering questions about your background and capturing leads in real-time.

## What is this?

Instead of a static PDF resume, this project creates an intelligent agent that:
- Answers questions about your professional background, skills, and experience
- Captures contact information from interested visitors
- Tracks questions it can't answer to help you improve
- Sends real-time push notifications for all interactions

## Architecture

This is an agentic AI system with a simple but effective structure:

**Head (Mind)**: OpenAI LLM
- Perceives and understands user questions
- Decides when to use tools autonomously
- Generates contextual responses

**Body (Actions)**: Tool System
- `record_user_details`: Captures leads when visitors want to connect
- `record_unknown_question`: Tracks knowledge gaps
- `NotificationSender`: Pushover integration for instant alerts

## Features

- Interactive chat interface powered by Gradio
- Custom knowledge base loaded from your personal data
- Real-time push notifications via Pushover
- Autonomous tool usage by the LLM
- Lead capture and unknown question tracking

## Getting Started

### Prerequisites

- Python 3.8+
- OpenAI API key
- Pushover account (user key + application token)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/AzizImani/virtual-resume.git
cd virtual-resume
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory:
```env
OPENAI_API_KEY=your_openai_api_key_here
PUSHOVER_USER_KEY=your_pushover_user_key
PUSHOVER_APP_TOKEN=your_pushover_app_token
```

5. Add your personal information in the `me/` folder (markdown files with your background, experience, skills, etc.)

### Running the Application

```bash
python src/app.py
```

The chatbot interface will be available at `http://127.0.0.1:7860`

## Project Structure

```
virtual-resume/
├── src/
│   ├── app.py                    # Main application logic
│   ├── personal_chatbot.py       # Chatbot orchestration
│   ├── knowledge_source.py       # Loads your personal data
│   ├── notification_sender.py    # Pushover integration
│   ├── system_prompt.py          # LLM system prompt
│   └── tools.py                  # Agent tools definition
├── me/                           # Your personal information (markdown files)
├── .env                          # Environment variables
├── requirements.txt              # Python dependencies
└── README.md
```

## How It Works

1. **User asks a question** → The chatbot receives the message
2. **LLM processes** → OpenAI analyzes the question against your knowledge base
3. **Autonomous decision** → The agent decides whether to:
   - Answer directly from knowledge
   - Use `record_user_details` tool if visitor wants to connect
   - Use `record_unknown_question` tool if answer is unknown
4. **Action execution** → Tools send you push notifications via Pushover
5. **Response** → User receives a helpful reply

## Customization

### Adding Your Information

Place markdown files in the `me/` folder with information about:
- Professional experience
- Skills and expertise
- Projects and achievements
- Education
- Contact preferences

### Adding New Tools

Extend the `Tools` class in `src/tools.py`:

```python
def your_new_tool(self, param1, param2):
    # Your tool logic here
    return {"status": "success"}
```

Add the tool definition to the `__tools` list with proper JSON schema.

## Learning Resources

This project was inspired by Ed Donner's course on Udemy about agentic AI systems: https://www.udemy.com/course/the-complete-agentic-ai-engineering-course

