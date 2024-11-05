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


class Catalog:
    """Manages the collection of e-books in the store."""

    def __init__(self):
        self._ebooks = []

    def add_ebook(self, ebook):
        self._ebooks.append(ebook)

    def remove_ebook(self, title):
        self._ebooks = [ebook for ebook in self._ebooks if ebook.get_title() != title]

    def display_catalog(self):
        return "\n".join(str(ebook) for ebook in self._ebooks)

    def __str__(self):
        return f"Catalog contains {len(self._ebooks)} e-books."


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


class Order:
    """Represents a customer's order."""

    def __init__(self, customer, shopping_cart, order_date):
        self._customer = customer
        self._shopping_cart = shopping_cart
        self._order_date = order_date
        self._is_completed = False

    def apply_discounts(self):
        base_price = self._shopping_cart.get_total_price()
        print(f"Base price before discounts: AED{base_price:.2f}")

        loyalty_discount = 0
        bulk_discount = 0

        if self._customer.is_loyalty_member():
            loyalty_discount = 0.10 * base_price  # 10% loyalty discount
            print("Loyalty discount applied: 10%")

        if len(self._shopping_cart._items) >= 5:
            bulk_discount = 0.20 * base_price  # 20% bulk discount
            print("Bulk purchase discount applied: 20%")

        # Apply only the highest applicable discount
        total_discount = max(loyalty_discount, bulk_discount)
        print(f"Total discount applied: AED{total_discount:.2f}")

        total_after_discount = base_price - total_discount
        vat = total_after_discount * 0.08  # 8% VAT
        print(f"VAT applied: AED{vat:.2f}")

        total_with_vat = total_after_discount + vat
        print(f"Total after discount and VAT: AED{total_with_vat:.2f}")

        return total_with_vat

    def complete_order(self):
        self._is_completed = True
        return self.apply_discounts()

    def __str__(self):
        return f"Order for {self._customer.get_name()} on {self._order_date}"


class Invoice:
    """Generates and displays an invoice for a completed order."""
    @staticmethod
    def generate(order):
        total_price = order.complete_order()
        print(f"Invoice for {order}")
        print(f"Total price (after discounts and VAT): AED{total_price:.2f}")


class Tests:
    @staticmethod
    def run_tests():
        # Create e-books
        ebook1 = EBook("Python Programming", "John Smith", "2023-01-01", "Programming", 25.00)
        ebook2 = EBook("Data Science", "Jane Doe", "2022-06-15", "Science", 30.00)
        ebook3 = EBook("Machine Learning", "Alan Turing", "2021-09-10", "Technology", 35.00)
        ebook4 = EBook("Artificial Intelligence", "Ada Lovelace", "2020-04-22", "Technology", 40.00)
        ebook5 = EBook("Deep Learning", "Geoffrey Hinton", "2019-08-17", "Science", 50.00)

        # Create and display catalog
        catalog = Catalog()
        catalog.add_ebook(ebook1)
        catalog.add_ebook(ebook2)
        catalog.add_ebook(ebook3)
        catalog.add_ebook(ebook4)
        catalog.add_ebook(ebook5)
        print("Catalog:")
        print(catalog)

        # Create a customer with loyalty program
        customer1 = Customer("Rashed Jasim", "RashJas@gmail.com", is_loyalty_member=True)
        print("\nCustomer Info:")
        print(customer1)

        # Add e-books to the shopping cart
        cart1 = ShoppingCart()
        cart1.add_item(ebook1)
        cart1.add_item(ebook2)
        cart1.add_item(ebook3)
        cart1.add_item(ebook4)
        cart1.add_item(ebook5)
        print("\nShopping Cart:")
        print(cart1)

        # Create and display an order
        order1 = Order(customer1, cart1, "2024-01-10")
        print("\nOrder Summary for Rashed Jasim:")
        print(order1)

        # Generate an invoice
        print("\nInvoice for Rashed Jasim:")
        Invoice.generate(order1)

        # Repeat for another customer without loyalty
        customer2 = Customer("Ali Salem", "ali@gmail.com", is_loyalty_member=False)
        cart2 = ShoppingCart()
        cart2.add_item(ebook1)
        cart2.add_item(ebook2)
        cart2.add_item(ebook3)
        cart2.add_item(ebook4)
        cart2.add_item(ebook5)
        order2 = Order(customer2, cart2, "2024-01-11")
        print("\nOrder Summary for Ali Salem:")
        print(order2)
        print("\nInvoice for Ali Salem:")
        Invoice.generate(order2)

        # Create a third customer with 2 books
        customer3 = Customer("Abdullah Hamad", "abdullah@gmail.com", is_loyalty_member=False)
        cart3 = ShoppingCart()
        cart3.add_item(ebook1)
        cart3.add_item(ebook2)
        order3 = Order(customer3, cart3, "2024-01-12")
        print("\nOrder Summary for Abdullah Hamad:")
        print(order3)
        print("\nInvoice for Abdullah Hamad:")
        Invoice.generate(order3)


# Call the test method from the class
Tests.run_tests()
