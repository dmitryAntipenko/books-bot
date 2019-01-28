from requests import get


class DataProvider:

    base_url = 'https://whatshouldireadnext.com'

    def get_books_list(self, book_name):
        response = get(self.base_url + '/finder.php?q=' + book_name)
        if response.status_code / 100 == 2:
            return response.text
        return None

    def get_recommendations(self, book_id):
        response = get(self.base_url + '/isbn/' + book_id)
        if response.status_code / 100 == 2:
            return response.text
        return None
