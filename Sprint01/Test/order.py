class Order:
    def __init__(self):
        self.orders = []

    def add_order(self, item):
        self.orders.append(item)

    def get_orders(self):
        return self.orders
