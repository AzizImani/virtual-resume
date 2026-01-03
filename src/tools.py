from src.notification_sender import NotificationSender
import json


class Tools:

    __record_user_details_json = {
        "name": "record_user_details",
        "description": "Use this tool to record that a user is interested in being in touch and provided an email address",
        "parameters": {
            "type": "object",
            "properties": {
                "email": {
                    "type": "string",
                    "description": "The email address of this user"
                },
                "name": {
                    "type": "string",
                    "description": "The user's name, if they provided it"
                }
                ,
                "notes": {
                    "type": "string",
                    "description": "Any additional information about the conversation that's worth recording to give context"
                }
            },
            "required": ["email"],
            "additionalProperties": False
        }
    }

    __record_unknown_question_json = {
        "name": "record_unknown_question",
        "description": "Always use this tool to record any question that couldn't be answered as you didn't know the answer",
        "parameters": {
            "type": "object",
            "properties": {
                "question": {
                    "type": "string",
                    "description": "The question that couldn't be answered"
                },
            },
            "required": ["question"],
            "additionalProperties": False
        }
    }

    __tools = [
        {"type": "function", "function": __record_user_details_json},
        {"type": "function", "function": __record_unknown_question_json}
    ]

    def __init__(self):
        self.notification_sender = NotificationSender()

    def record_user_details(self, email, name="Name not provided", notes="not provided"):
        self.notification_sender.push(f"Recording interest from {name} with email {email} and notes {notes}")
        return {"recorded": "ok"}

    def record_unknown_question(self, question):
        self.notification_sender.push(f"Recording {question} asked that I couldn't answer")
        return {"recorded": "ok"}

    def get_tools(self):
        return self.__tools

    def handle_tool_calls(self, tool_calls):
        results = []
        for tool_call in tool_calls:
            tool_name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)
            print(f"Tool called: {tool_name}", flush=True)
            tool = getattr(self, tool_name, None)
            result = tool(**arguments) if tool else {}
            results.append({"role": "tool", "content": json.dumps(result), "tool_call_id": tool_call.id})
        return results
