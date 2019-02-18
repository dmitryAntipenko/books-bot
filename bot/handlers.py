from . import data_provider
from .decorators import message_handler
from bs4 import BeautifulSoup


@message_handler
def handle_book(bot, update):
    response = data_provider.get_books_list(update.message.text)

    if response is not None:
        soup = BeautifulSoup(response, 'html.parser')
        anchors = soup.find_all('a')

        result = ''

        for anchor in anchors:
            identifier = anchor.get('href')
            title = anchor.get_text()
            identifier = identifier.split('isbn/')
            result += f'*{title}*\n /bk{identifier[1]}\n\n'


        if len(result) > 0:
            return result

    return "Sorry :("


@message_handler
def handle_recommendation(bot, update):
    book_id = update.message.text.split('/bk')[1]
    response = data_provider.get_recommendations(book_id)

    if response is not None:
        soup = BeautifulSoup(response, 'html.parser')
        recommendations = soup.findAll('li', {'class': 'recommendation-logged-out'})
        recommended_books = [r.get_text() for r in recommendations]

        if len(recommended_books) > 0:
            str = ''
            for book in recommended_books:
                str += f'*{book}*\n'
            return str

    return "Sorry :("
