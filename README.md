# Description
Basic library to send a Telegram message via Python script

This is useful when you let a script running and want to receive a notification when finished.

# To use it

## Get Telegram bot token and chat_id
Use `BotFather` to create a new bot. Start a conversation and follow instructions.
Here you will get your bot_token.

To get your `chat_id`, go to the following link in your browser using your bot_token

```
https://api.telegram.org/{bot_token}/getUpdates
```

You will get your chat id from something like this:

```
{
    "ok": true,
        "result": [
            {
                "chat": {
                    "id": <HERE_IS_YOUR_CHAT_ID>,
                    "first_name": "Rodrigo",
                    "last_name": "Zapata",
                    "type": "private"
                }
                ...
            }
        ]
    }
}

```

## Set it up in your project
Paste this in your requirements file
```
git+https://github.com/yourusername/notifyme.git@v1.0.0#egg=notifyme
```

Then you use it in your script as

```
from notifier.telegram_notifier import TelegramNotifier

notifier = TelegramNotifier(bot_token, chat_id)
notifier.send_message("Hello from NotifyMe!")
```
