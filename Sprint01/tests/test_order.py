import unittest
from modules.order import Order

class TestOrder(unittest.TestCase):
    def test_add_order(self):
        order = Order()
        order.add_order("Pizza")
        self.assertIn("Pizza", order.get_orders())

if __name__ == "__main__":
    unittest.main()
