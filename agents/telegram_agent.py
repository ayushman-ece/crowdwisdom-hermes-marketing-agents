from services.telegram_service import TelegramService


class TelegramAgent:

    def __init__(self):

        self.telegram = TelegramService()

    def send(self, message):

        self.telegram.send(message)