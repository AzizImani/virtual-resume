from openai import OpenAI

from src.tools import Tools


class PersonalChatbot:

    def __init__(self, client: OpenAI, system_prompt: str, tools: Tools):
        self.client = client
        self.system_prompt = system_prompt
        self.tools = tools

    def chat(self, message, history):
        messages = [{"role": "system", "content": self.system_prompt}] + history + [{"role": "user", "content": message}]
        done = False
        response = ''
        while not done:

            response = self.client.chat.completions.create(model="gpt-4o-mini", messages=messages, tools=self.tools.get_tools())

            finish_reason = response.choices[0].finish_reason

            # If the LLM wants to call a tool, we do that!

            if finish_reason == "tool_calls":
                message = response.choices[0].message
                tool_calls = message.tool_calls
                results = self.tools.handle_tool_calls(tool_calls)
                messages.append(message)
                messages.extend(results)
            else:
                done = True

        return response.choices[0].message.content
