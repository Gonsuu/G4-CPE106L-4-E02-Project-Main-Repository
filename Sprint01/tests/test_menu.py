import unittest
from modules.menu import Menu

class TestMenu(unittest.TestCase):
    def test_get_items(self):
        menu = Menu()
        self.assertIn("Burger", menu.get_items())

if __name__ == "__main__":
    unittest.main()
