import time
import threading
import requests

import requests

from config.config import OLLAMA_URL, MODEL

running = False

def loading(start):
    animations = ["|", "/", "-", "\\"]
    i = 0
    
    while running:
        elapsed = time.perf_counter() - start
        
        print(f"\r{animations[i % 4]} charles está pensando... {elapsed:.1f}s", end="", flush=True)
        
        i += 1
        time.sleep(0.1)


def chat(messages):
    
    global running
    
    start = time.perf_counter()
    
    running = True
    
    thread = threading.Thread(target=loading, args=(start,))
    thread.start()

    response = requests.post(
        f"{OLLAMA_URL}/api/chat",
        json={
            "model": MODEL,
            "messages": messages,
            "stream": False,
            "think": False,
            "format": "json"
        },
        timeout=300
    )
    
    running = False
    thread.join()
    
    elapsed = time.perf_counter() - start
    
    print(f"\r✓ Ollama respondeu em {elapsed:.2f}s          ")
    
    response.raise_for_status()

    data = response.json()

    data["_elapsed"] = elapsed

    return data