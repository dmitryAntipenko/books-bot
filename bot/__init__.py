from telegram.ext import Updater, messagequeue
from .data_provider import DataProvider
from .bot import BooksBot
import os

token = os.environ.get('TOKEN')

queue = messagequeue.MessageQueue(all_burst_limit=3, all_time_limit_ms=3000)
books_bot = BooksBot(mqueue=queue, token=token)
updater = Updater(bot=books_bot)
data_provider = DataProvider()
