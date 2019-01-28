from telegram.ext import messagequeue
from telegram import bot


class BooksBot(bot.Bot):

    def __init__(self, *args, is_queued_def=True, mqueue=None, **kwargs):
        super(BooksBot, self).__init__(*args, **kwargs)
        self._is_messages_queued_default = is_queued_def
        self._msg_queue = mqueue or messagequeue.MessageQueue()

    def __del__(self):
        try:
            self._msg_queue.stop()
        except:
            pass

        super(BooksBot, self).__del__()

    @messagequeue.queuedmessage
    def send_message(self, *args, **kwargs):
        return super(BooksBot, self).send_message(*args, **kwargs)
