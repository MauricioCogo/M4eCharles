from src.ollama_client import chat
from config.config import SYSTEM_PROMPT



class Charles:

    def __init__(self):
        self.messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]

    def ask(self, prompt):
        self.messages.append({
            "role": "user",
            "content": prompt
        })

        response = chat(self.messages)

        message = response["message"]

        self.messages.append({
            "role": "assistant",
            "content": message["content"]
        })

        print(f"[Ollama: {response['_elapsed']:.2f}s]")

        return message["content"]