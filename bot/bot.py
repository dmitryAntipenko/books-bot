from telegram.ext import messagequeue
from telegram import bot


class BooksBot(bot.Bot):

    def __init__(self, *args, is_queued_def=True, mqueue=None, **kwargs):
        super().__init__(*args, **kwargs)
        self._is_messages_queued_default = is_queued_def
        self._msg_queue = mqueue or messagequeue.MessageQueue()

    def __del__(self):
        try:
            self._msg_queue.stop()
        except:
            pass


    @messagequeue.queuedmessage
    def send_message(self, *args, **kwargs):
        return super().send_message(*args, **kwargs)
