#Menu module
class Menu:
    def __init__(self):
        self.menu_items = []
        self.book_table = []
        self.customer_orders = []

    def add_item_to_menu(self, item, price, tag):
        self.menu_items.append({"Name": item, "Price": price, "Tag": tag})

    def print_menu(self):
        print("-"*30)
        print("Quick-Eats Menu")
        print("-"*30)
        for item in self.menu_items:
            print(f"#{item['Tag']} - {item['Name']} - {item['Price']}")
        print("-"*30)

    def find_item(self, tag):
        return next((item for item in self.menu_items if item["Tag"] == tag), None)

menu = Menu()

# menu items
menu_list = [
    {"Name": "Classic Cheeseburger", "Price": "₱95", "Tag": 1},
    {"Name": "Margherita Pizza", "Price": "₱440", "Tag": 2},
    {"Name": "Grilled Chicken Caesar Salad", "Price": "₱200", "Tag": 3},
    {"Name": "Spicy Chicken Tacos (2pcs)", "Price": "₱140", "Tag": 4},
    {"Name": "Vegetable Stir-Fry", "Price": "₱140", "Tag": 5},
    {"Name": "Fish and Chips", "Price": "₱120", "Tag": 6},
    {"Name": "Mushroom Risotto", "Price": "₱180", "Tag": 7},
    {"Name": "BBQ Pulled Pork Sandwich", "Price": "₱120", "Tag": 8},
    {"Name": "Caprese Panini", "Price": "₱80", "Tag": 9},
    {"Name": "Chocolate Lava Cake", "Price": "₱200", "Tag": 10},
]

for item in menu_list:
    menu.add_item_to_menu(item["Name"], item["Price"], item["Tag"])
