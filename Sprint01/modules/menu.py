class Menu:
    def __init__(self):
        self.menu_items = []

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
