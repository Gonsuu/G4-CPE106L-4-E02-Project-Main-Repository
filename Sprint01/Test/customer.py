import random
from order import Order

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
        menu.print_menu()
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
