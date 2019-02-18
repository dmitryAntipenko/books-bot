from telegram.ext import BaseFilter


class RecommendationFilter(BaseFilter):
    def filter(self, message):
        return message.text.startswith('/bk')
