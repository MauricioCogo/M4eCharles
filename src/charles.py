from src.ollama_client import chat

from config.config import SYSTEM_PROMPT
from src.memory import Memory

from src.memory_detector import MemoryDetector

import json

class Charles:

    def __init__(self):
        self.memory = Memory()
        self.memory_detector = MemoryDetector()
        
        self.messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]

    def build_memory_context(self):
        memories = self.memory.get_all()
        
        if not memories:
            return ""
        
        memory_text = "\n".join(
            f"- {memory['content']}"
            for memory in memories
        )
        
        return f"""
            MEMÓRIAS DISPONÍVEIS:
            {memory_text}
            Estas memórias servem apenas como contexto interno.
            Use somente as memórias relevantes para responder à pergunta atual.
            Não liste todas as memórias.
            Não resuma as memórias.
            Não mencione informações irrelevantes.
            Se nenhuma memória for relevante, ignore todas elas.
            """

    def ask(self, prompt):
        memory_context = self.build_memory_context()
        
        request_messages = [self.messages[0]]  # Start with the system prompt
        
        if memory_context:
            request_messages.append({
                "role": "system",
                "content": memory_context
            })
        
        request_messages.extend(self.messages[1:])  # Add previous messages (user and assistant)
        
        request_messages.append({
            "role": "user",
            "content": prompt
        })
        
        response = chat(request_messages)
        
        raw_content = response["message"]["content"]

        result = json.loads(raw_content)

        answer = result["answer"]
        memory_candidate = result.get("memory")
        
        self.messages.append({
            "role": "user",
            "content": prompt
        })
        
        self.messages.append({
            "role": "assistant",
            "content": answer
        })

        return answer, memory_candidate
    
    def detect_memory(self, prompt):
        return self.memory_detector.detect(prompt)
        