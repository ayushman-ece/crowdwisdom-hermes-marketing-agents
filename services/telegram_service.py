import requests

from config import TELEGRAM_BOT_TOKEN
from config import TELEGRAM_CHAT_ID


class TelegramService:

    def send(self, message: str):

        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

        requests.post(

            url,

            json={

                "chat_id": TELEGRAM_CHAT_ID,

                "text": message

            }

        )