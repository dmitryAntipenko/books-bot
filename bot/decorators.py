from . import books_bot
from telegram import ParseMode


def message_handler(func):
    def wrapper(*args, **kwargs):
        text = func(*args, **kwargs)
        books_bot.send_message(chat_id=args[1].message.chat_id, text=text, parse_mode=ParseMode.MARKDOWN)
    return wrapper
