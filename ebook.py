    class EBook:
    """Represents an e-book in the store."""

    def __init__(self, title, author, publication_date, genre, price):
        self.__title = title
        self.__author = author
        self.__publication_date = publication_date
        self.__genre = genre
        self.__price = price

    def get_title(self):
        return self.__title

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if price > 0:
            self.__price = price
        else:
            raise ValueError("Price must be greater than zero")

    def __str__(self):
        return f"EBook: {self.__title} by {self.__author}, AED{self.__price:.2f}"
