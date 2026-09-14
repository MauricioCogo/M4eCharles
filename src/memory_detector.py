from src.ollama_client import chat


class MemoryDetector:

    def detect(self, prompt):
        messages = [
            {
                "role": "system",
                "content": """
                    Analise a mensagem do usuário.

                    Determine se existe alguma informação que seria útil lembrar
                    em conversas futuras.

                    Informações que podem ser memorizadas:
                    - informações sobre o usuário;
                    - preferências;
                    - decisões sobre projetos;
                    - tecnologias utilizadas;
                    - objetivos de longo prazo;
                    - informações persistentes sobre projetos.

                    Não memorize:
                    - perguntas;
                    - cumprimentos;
                    - informações temporárias;
                    - comandos;
                    - frases sem valor futuro.

                    Responda exatamente neste formato:

                    MEMORY: texto da memória

                    ou:

                    MEMORY: NONE
                """,
            },
            {"role": "user", "content": prompt},
        ]
        
        response = chat(messages)
        
        content = response["message"]["content"].strip()
        
        if content.startswith("MEMORY:"):
            memory = content.replace("MEMORY:", "", 1).strip()
            
            if memory == "NONE":
                return None
            
            return memory
        
        return None
