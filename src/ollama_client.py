import time

import requests

from config.config import OLLAMA_URL, MODEL


def chat(messages):
    
    print("\n --- mensagens enviadas ---")
    for msg in messages:
        print(f"  {msg['role']}: {msg['content']}")

    print("\n --- --- ---")
    start = time.perf_counter()

    response = requests.post(
        f"{OLLAMA_URL}/api/chat",
        json={
            "model": MODEL,
            "messages": messages,
            "stream": False,
            "think": False
        },
        timeout=300
    )

    elapsed = time.perf_counter() - start

    response.raise_for_status()

    data = response.json()

    data["_elapsed"] = elapsed

    return data