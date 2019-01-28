from . import data_provider
from .decorators import message_handler
from dataclasses import dataclass
from bs4 import BeautifulSoup


@dataclass
class Book:
    # author: str
    title: str
    ref: str


@message_handler
def handle_book(bot, update):
    response = data_provider.get_books_list(update.message.text)

    if response is not None:
        soup = BeautifulSoup(response, 'html.parser')
        anchors = soup.find_all('a')

        books = []

        for anchor in anchors:
            href = anchor.get('href')
            title = anchor.get_text()
            book = Book(title, href)

            books.append(book)

        if len(books) != 0:
            return '{}'.format(books)

    return "Sorry :("
