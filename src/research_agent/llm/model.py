import requests

from research_agent.config.settings import LLAMA_BASE_URL, MODEL, TEMP


def generate_response(prompt: str) -> str:
    response = requests.post(
        f"{LLAMA_BASE_URL}/v1/chat/completions",
        json={
            "model": MODEL,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": TEMP,
        },
        timeout=120
    )

    response.raise_for_status()

    data = response.json()

    return data["choices"][0]["message"]["content"]

