from bot import updater
from bot import handlers
from telegram.ext import MessageHandler, Filters
from bot.filters import RecommendationFilter


if __name__ == '__main__':
    updater.dispatcher.add_handler(MessageHandler(Filters.text, handlers.handle_book))
    updater.dispatcher.add_handler(MessageHandler(RecommendationFilter(), handlers.handle_recommendation))

    updater.start_polling()
    updater.idle()
