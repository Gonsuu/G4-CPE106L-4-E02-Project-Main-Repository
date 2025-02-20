class Customer:
    def __init__(self, name):
        self.name = name
        self.order = []
    
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
                    self.order.append(item)
                    print(f"✔ {item['Name']} added to your order.")
                else:
                    print("❌ Invalid tag number. Please try again.")
            except ValueError:
                print("❌ Invalid input. Please enter a number.")
    
    def view_order(self):
        if not self.order:
            print("\n🛒 Your order is empty.")
        else:
            print("\n======== Your Order Summary ========")
            total_price = sum(int(item["Price"][1:]) for item in self.order)
            for idx, item in enumerate(self.order, start=1):
                print(f"{idx}. {item['Name']} - {item['Price']}")
            print(f"\n💰 Total Price: ₱{total_price}")
            print("=====================================")
    
    def remove_item(self):
        if not self.order:
            print("\n🛒 Your order is empty. Nothing to remove.")
            return

        self.view_order()
        try:
            item_number = int(input("Enter the number of the item to remove: "))
            if 0 < item_number <= len(self.order):
                removed_item = self.order.pop(item_number - 1)
                print(f"❌ Removed {removed_item['Name']} from your order.")
            else:
                print("❌ Invalid item number.")
        except ValueError:
            print("❌ Invalid input. Please enter a number.")
    
    def submit_order(self):
        if not self.order:
            print("\n❌ You cannot submit an empty order.")
        else:
            self.view_order()
            print("\n✅ Order submitted successfully!")
            self.order.clear()
    
    def request_waiter(self):
        print("\n🔔 Waiter requested for manual billing.")
