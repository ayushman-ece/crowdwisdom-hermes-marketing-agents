import requests

from config import OPENROUTER_API_KEY
from config import MODEL

from services.logger import logger


class OpenRouterService:

    URL = "https://openrouter.ai/api/v1/chat/completions"

    def ask(self, prompt: str):

        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        }

        body = {
            "model": MODEL,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }

        response = requests.post(
            self.URL,
            headers=headers,
            json=body,
            timeout=120
        )

        response.raise_for_status()

        answer = response.json()["choices"][0]["message"]["content"]

        logger.info("LLM Response Generated")

        return answer