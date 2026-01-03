from openai import OpenAI


class PersonalChatbot:

    def __init__(self, client: OpenAI, system_prompt: str):
        self.client = client
        self.system_prompt = system_prompt

    def chat(self, message, history):
        messages = [{"role": "system", "content": self.system_prompt}] + history + [{"role": "user", "content": message}]
        response = self.client.chat.completions.create(model="gpt-4o-mini", messages=messages)
        return response.choices[0].message.content
