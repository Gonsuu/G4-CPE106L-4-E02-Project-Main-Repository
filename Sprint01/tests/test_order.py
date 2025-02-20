import unittest
from modules.order import Order

class TestOrder(unittest.TestCase):
    def setUp(self):
        """Create a fresh Order instance before each test."""
        self.order = Order()

    def test_add_single_order(self):
        """Test if a single item can be added to the order."""
        item = {"Name": "Classic Cheeseburger", "Price": "₱95", "Tag": 1}
        self.order.add_order(item)
        self.assertEqual(self.order.get_orders(), [item])

    def test_add_multiple_orders(self):
        """Test if multiple items can be added to the order."""
        items = [
            {"Name": "Classic Cheeseburger", "Price": "₱95", "Tag": 1},
            {"Name": "Margherita Pizza", "Price": "₱440", "Tag": 2},
        ]
        for item in items:
            self.order.add_order(item)

        self.assertEqual(self.order.get_orders(), items)

    def test_get_orders_empty(self):
        """Test if get_orders() returns an empty list when no items are added."""
        self.assertEqual(self.order.get_orders(), [])

if __name__ == '__main__':
    unittest.main()
