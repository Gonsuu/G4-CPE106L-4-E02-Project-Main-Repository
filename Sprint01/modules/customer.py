from modules.order import Order  # Import Order class

class Customer:
    def __init__(self, name):
        self.name = name
        self.order = Order()  # Use Order class for managing orders

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
                    self.order.add_order(item)  # Use Order class to add item
                    print(f"✔ {item['Name']} added to your order.")
                else:
                    print("❌ Invalid tag number. Please try again.")
            except ValueError:
                print("❌ Invalid input. Please enter a number.")

    def view_order(self):
        orders = self.order.get_orders()  # Get orders from Order class
        if not orders:
            print("\n🛒 Your order is empty.")
        else:
            print("\n======== Your Order Summary ========")
            total_price = sum(int(item["Price"][1:]) for item in orders)
            for idx, item in enumerate(orders, start=1):
                print(f"{idx}. {item['Name']} - {item['Price']}")
            print(f"\n💰 Total Price: ₱{total_price}")
            print("=====================================")

    def remove_item(self):
        orders = self.order.get_orders()
        if not orders:
            print("\n🛒 Your order is empty. Nothing to remove.")
            return

        self.view_order()
        try:
            item_number = int(input("Enter the number of the item to remove: "))
            if 0 < item_number <= len(orders):
                removed_item = orders.pop(item_number - 1)
                print(f"❌ Removed {removed_item['Name']} from your order.")
            else:
                print("❌ Invalid item number.")
        except ValueError:
            print("❌ Invalid input. Please enter a number.")

    def submit_order(self):
        orders = self.order.get_orders()
        if not orders:
            print("\n❌ You cannot submit an empty order.")
        else:
            self.view_order()
            print("\n✅ Order submitted successfully!")
            self.order.orders.clear()  # Clear order after submission

    def request_waiter(self):
        print("\n🔔 Waiter requested for manual billing.")
