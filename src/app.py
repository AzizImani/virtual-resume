import gradio as gr
from dotenv import load_dotenv
from openai import OpenAI

from knowledge_source import KnowledgeSource
from personal_chatbot import PersonalChatbot
from src.tools import Tools
from system_prompt import SystemPrompt


if __name__ == '__main__':
    load_dotenv(override=True)

    system_prompt = SystemPrompt().create_system_prompt()

    chatbot = PersonalChatbot(OpenAI(), system_prompt, Tools())

    interface = gr.ChatInterface(
        fn=chatbot.chat,
        title=f"Chat with {KnowledgeSource.load_name()}",
        description=f"Ask me about my background, experience, and skills!",
        examples=[
            "Tell me about your experience",
            "What are your key skills?",
            "What projects have you worked on?",
        ]
    )

    interface.launch()
