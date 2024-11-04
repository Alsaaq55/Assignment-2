class Customer:
    """Represents a customer of the e-bookstore."""

    def __init__(self, name, contact_info, is_loyalty_member=False):
        self._name = name
        self._contact_info = contact_info
        self._is_loyalty_member = is_loyalty_member

    def get_name(self):
        return self._name

    def is_loyalty_member(self):
        return self._is_loyalty_member

    def __str__(self):
        return f"Customer: {self._name}, Loyalty Member: {self._is_loyalty_member}"
