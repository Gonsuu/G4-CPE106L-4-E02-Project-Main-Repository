from modules.menu import Menu
from modules.customer import Customer  # Import the Customer class

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
customer = Customer(name="Guest")

# Instructions
def instructions():
    print('-' * 30)
    print("Welcome to Quick-Eats!")
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
        print("👋 Thank you for using Quick Eats! Goodbye!")
        break
    else:
        print("❌ Invalid choice. Please try again.")
