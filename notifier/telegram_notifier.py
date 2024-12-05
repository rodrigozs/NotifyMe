import requests
from dotenv import load_dotenv
import os

load_dotenv()


class TelegramNotifier:
    def __init__(self):
        """
        Initialize the TelegramNotifier with bot token and chat ID.

        :param bot_token: The token for your Telegram bot.
        :param chat_id: Your chat ID.
        """
        self.bot_token = os.getenv("BOT_TOKEN")
        self.chat_id = os.getenv("CHAT_ID")

        print(self.bot_token, self.chat_id)

    def send_message(self, message: str):
        """
        Send a message to the specified Telegram chat.

        :param message: The message to send.
        :raises Exception: If the message fails to send.
        """
        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
        payload = {"chat_id": self.chat_id, "text": message}

        response = requests.post(url, json=payload)

        if not response.ok:
            raise Exception(f"Failed to send message: {response.text}")


# Example usage (Uncomment to test directly):
if __name__ == "__main__":
    notifier = TelegramNotifier()
    notifier.send_message("Hello from Python!")
