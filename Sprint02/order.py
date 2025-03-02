class Order:
    def __init__(self):
        self.orders = []

    def add_order(self, item):
        """Adds an item to the order."""
        self.orders.append(item)

    def get_orders(self):
        """Returns the list of ordered items."""
        return self.orders

    def remove_order(self, index):
        """Removes an item from the order using its index."""
        if 0 <= index < len(self.orders):
            return self.orders.pop(index)  # Remove and return the item
        else:
            return None  # Invalid index

    def clear_order(self):
        """Clears all items from the order."""
        self.orders.clear()

    def get_total_price(self):
        """Calculates the total price of the order."""
        return sum(int(item["Price"][1:]) for item in self.orders) if self.orders else 0
