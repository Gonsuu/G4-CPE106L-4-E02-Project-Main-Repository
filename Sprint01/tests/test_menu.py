import unittest
from menu import Menu

class TestMenu(unittest.TestCase):
    def setUp(self):
        self.menu = Menu()
        self.menu.add_item_to_menu("Classic Cheeseburger", "₱95", 1)
        self.menu.add_item_to_menu("Margherita Pizza", "₱440", 2)

    def test_add_item_to_menu(self):
        self.assertEqual(len(self.menu.menu_items), 2)
        self.assertEqual(self.menu.menu_items[0]["Name"], "Classic Cheeseburger")
        self.assertEqual(self.menu.menu_items[1]["Price"], "₱440")

    def test_find_item_existing(self):
        item = self.menu.find_item(1)
        self.assertIsNotNone(item)
        self.assertEqual(item["Name"], "Classic Cheeseburger")

    def test_find_item_non_existent(self):
        item = self.menu.find_item(99)
        self.assertIsNone(item)

    def test_print_menu(self):
        expected_output = (
            "-" * 30 + "\n"
            "Quick-Eats Menu\n" +
            "-" * 30 + "\n"
            "#1 - Classic Cheeseburger - ₱95\n"
            "#2 - Margherita Pizza - ₱440\n"
            "-" * 30 + "\n"
        )
        from io import StringIO
        import sys
        captured_output = StringIO()
        sys.stdout = captured_output
        self.menu.print_menu()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == "__main__":
    unittest.main()
