from shopping_cart import ShoppingCart
from customer import Customer


class Order:
    """Represents a customer's order."""

    def __init__(self, customer, shopping_cart, order_date):
        self._customer = customer
        self._shopping_cart = shopping_cart
        self._order_date = order_date
        self._is_completed = False

    def apply_discounts(self):
        base_price = self._shopping_cart.get_total_price()
        discount = 0
        if self._customer.is_loyalty_member():
            discount = 0.10 * base_price  # 10% loyalty discount
        if len(self._shopping_cart._items) >= 5:
            discount = max(discount, 0.20 * base_price)  # 20% bulk discount
        return base_price - discount

    def complete_order(self):
        self._is_completed = True
        return self.apply_discounts() * 1.08  # 8% VAT

    def __str__(self):
        return f"Order for {self._customer.get_name()} on {self._order_date}"
