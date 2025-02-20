import unittest
from modules.menu import Menu

class TestMenu(unittest.TestCase):
    def setUp(self):
        """Create a fresh Menu instance before each test."""
        self.menu = Menu()

    def test_add_single_item(self):
        """Test if a single item can be added to the menu."""
        self.menu.add_item_to_menu("Classic Cheeseburger", "₱95", 1)
        expected = [{"Name": "Classic Cheeseburger", "Price": "₱95", "Tag": 1}]
        self.assertEqual(self.menu.menu_items, expected)

    def test_add_multiple_items(self):
        """Test if multiple items can be added to the menu."""
        items = [
            ("Classic Cheeseburger", "₱95", 1),
            ("Margherita Pizza", "₱440", 2),
        ]
        for name, price, tag in items:
            self.menu.add_item_to_menu(name, price, tag)

        expected = [
            {"Name": "Classic Cheeseburger", "Price": "₱95", "Tag": 1},
            {"Name": "Margherita Pizza", "Price": "₱440", "Tag": 2},
        ]
        self.assertEqual(self.menu.menu_items, expected)

    def test_find_existing_item(self):
        """Test if an item can be found by its tag."""
        self.menu.add_item_to_menu("Spicy Chicken Tacos", "₱140", 3)
        item = self.menu.find_item(3)
        expected = {"Name": "Spicy Chicken Tacos", "Price": "₱140", "Tag": 3}
        self.assertEqual(item, expected)

    def test_find_non_existent_item(self):
        """Test if finding a non-existent tag returns None."""
        self.menu.add_item_to_menu("Grilled Chicken Salad", "₱200", 4)
        item = self.menu.find_item(99)  # Tag does not exist
        self.assertIsNone(item)

    def test_find_item_empty_menu(self):
        """Test if find_item returns None when the menu is empty."""
        self.assertIsNone(self.menu.find_item(1))

if __name__ == '__main__':
    unittest.main()

