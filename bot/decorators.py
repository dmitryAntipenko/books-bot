from . import books_bot


def message_handler(func):
    def wrapper(*args, **kwargs):
        text = func(*args, **kwargs)
        books_bot.send_message(chat_id=args[1].message.chat_id, text=text)
    return wrapper
