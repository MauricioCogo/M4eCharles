import json 
from pathlib import Path

MEMORY_FILE = Path("data/memory.json")

class Memory:
    
    def load (self):
        if not MEMORY_FILE.exists():
            print("não existe arquivo")
            return []
        
        with open(MEMORY_FILE, "r", encoding="utf-8") as file:
        
            return json.load(file)
        
    def save(self, memories):
        with open(MEMORY_FILE, "w", encoding="utf-8") as file:
            json.dump(memories, file, ensure_ascii=False, indent=4)
            
    def add(self, content):
        memories = self.load()
        
        memories.append({"content": content})
        
        self.save(memories)
    
    def get_all(self):
        return self.load()
    
