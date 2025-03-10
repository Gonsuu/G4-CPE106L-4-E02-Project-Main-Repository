class Menu:
    def __init__(self):
        # List of menu items
        self.items = [
            {"name": "Classic Cheeseburger", "price": "₱95", "tag": 1},
            {"name": "Margherita Pizza", "price": "₱440", "tag": 2},
            {"name": "Grilled Chicken Caesar Salad", "price": "₱200", "tag": 3},
            {"name": "Spicy Chicken Tacos (2pcs)", "price": "₱140", "tag": 4},
            {"name": "Vegetable Stir-Fry", "price": "₱140", "tag": 5},
            {"name": "Fish and Chips", "price": "₱120", "tag": 6},
            {"name": "Mushroom Risotto", "price": "₱180", "tag": 7},
            {"name": "BBQ Pulled Pork Sandwich", "price": "₱120", "tag": 8},
            {"name": "Caprese Panini", "price": "₱80", "tag": 9},
            {"name": "Chocolate Lava Cake", "price": "₱200", "tag": 10},
        ]

    def get_menu_items(self):
        """Return the list of menu items."""
        return self.items

    def print_menu(self):
        """Print the menu in a simple format."""
        print("\n📜 MENU 📜")
        for item in self.items:
            print(f"{item['tag']}. {item['name']} - {item['price']}")
        print()
