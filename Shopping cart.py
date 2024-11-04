from ebook import EBook

class ShoppingCart:
    """Manages items that a customer adds to their shopping cart."""

    def __init__(self):
        self._items = []

    def add_item(self, ebook):
        self._items.append(ebook)

    def remove_item(self, title):
        self._items = [item for item in self._items if item.get_title() != title]

    def get_total_price(self):
        return sum(item.get_price() for item in self._items)

    def __str__(self):
        return "\n".join(str(item) for item in self._items)
