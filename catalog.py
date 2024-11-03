from ebook import EBook

class Catalog:
    """Manages the collection of e-books in the store."""
    def __init__(self):
        self.ebooks = []

    def add_ebook(self, ebook):
        self._ebook.append(ebook)

    def remove_ebook(self, title):
        self._ebook = [ebook for ebook in self._ebooks if ebook.get_title() != title]

    def display_catalog(self):
        return "\n".join(str(ebook) for ebook in self._ebook)

    def __str__(self):
        return f"Catalog contain {len(self._ebooks)} e-books."
