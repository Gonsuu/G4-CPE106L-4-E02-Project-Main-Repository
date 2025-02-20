import random

class Customer:
    def __init__(self, name):
        self.name = name
        self.order = Order()
        self.order_id = self.generate_order_id()  # Generate a unique Order ID

    def generate_order_id(self):
        """Generates a random 6-digit Order ID."""
        return f"QE-{random.randint(100000, 999999)}"

    def browse_menu(self, menu):
        menu.print_menu()

    def place_order(self, menu):
        while True:
            try:
                tag = int(input("\nEnter (#) number of the item to add (0 to finish order): "))
                if tag == 0:
                    print("Returning to main menu...\n")
                    break

                item = menu.find_item(tag)
                if item:
                    self.order.add_order(item)  
                    print(f"✔ {item['Name']} added to your order.")
                else:
                    print("❌ Invalid tag number. Please try again.")
            except ValueError:
                print("❌ Invalid input. Please enter a number.")

    def view_order(self):
        orders = self.order.get_orders()  
        if not orders:  
            print("\n🛒 Your order is empty.")
        else:
            print(f"\n======== Order Summary for {self.name} (Order ID: {self.order_id}) ========")
            total_price = sum(int(item["Price"][1:]) for item in orders)
            for idx, item in enumerate(orders, start=1):
                print(f"{idx}. {item['Name']} - {item['Price']}")
            print(f"\n💰 Total Price: ₱{total_price}")
            print("=====================================")

    def submit_order(self):
        orders = self.order.get_orders()
        if not orders:
            print("\n❌ You cannot submit an empty order.")
        else:
            self.view_order()
            print(f"\n✅ {self.name}, your order has been submitted successfully!")
            print(f"📄 Your Order ID is: {self.order_id}")
            self.order.orders.clear()  

    def request_waiter(self):
        print("\n🔔 Waiter requested for manual billing.")
    def remove_item(self):
        orders = self.order.get_orders()
        if not orders:
            print("\n🛒 Your order is empty. Nothing to remove.")
            return

        self.view_order()  # Show the current order before removing
        try:
            item_number = int(input("Enter the number of the item to remove (0 to cancel): "))
            if item_number == 0:
                print("Returning to main menu...\n")
                return
            if 0 < item_number <= len(orders):
                removed_item = orders.pop(item_number - 1)
                print(f"❌ Removed {removed_item['Name']} from your order.")
            else:
                print("❌ Invalid item number. Please try again.")
        except ValueError:
            print("❌ Invalid input. Please enter a number.")



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


class Order:
    def __init__(self):
        self.orders = []

    def add_order(self, item):
        self.orders.append(item)

    def get_orders(self):
        return self.orders




# Initialize menu
menu = Menu()

# Sample menu items
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

# Add items to the menu
for item in menu_list:
    menu.add_item_to_menu(item["Name"], item["Price"], item["Tag"])

# Create a customer instance
customer_name = input("Please enter your name: ").strip() or "Guest"
customer = Customer(name=customer_name)


# Instructions
def instructions():
    print('-' * 30)
    print(f"Welcome to Quick-Eats, {customer.name}!")
    print('-' * 30)
    print("S : Show Menu")
    print("P : Place / Add an Order")
    print("O : Order Summary")
    print("R : Remove Item From Order")
    print("T : Submit Your Order")
    print("W : Request Waiter for Manual Billing")
    print("quit : Quit The Program")
    print('-' * 30)

# Main loop
while True:
    instructions()
    choice = input("Enter your choice: ").strip().lower()

    if choice == "s":
        customer.browse_menu(menu)
        input("Press 'Enter' to return...")
    elif choice == "p":
        customer.place_order(menu)
    elif choice == "o":
        customer.view_order()
        input("Press 'Enter' to return...")
    elif choice == "r":
        customer.remove_item()
    elif choice == "t":
        customer.submit_order()
    elif choice == "w":
        customer.request_waiter()
    elif choice == "quit":
        print(f"👋 Thank you for using Quick Eats, {customer.name}! Goodbye!")
        break
    else:
        print("❌ Invalid choice. Please try again.")
