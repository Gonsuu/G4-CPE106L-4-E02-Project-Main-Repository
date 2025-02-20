from modules.menu import Menu
#from modules.order import Order

customer_order = []

#instructions
def instructions():
    print('-'*30)
    print("Welcome to Quick-Eats!")
    print('-'*30)
    print("S : Show Menu")
    print("P : Place / Add an Order")
    print("O : Order Summary")
    print("R : Remove Item From Order")
    print("A : Add Item From Order")
    print("T : Submit Your Order")
    print("quit : Quit The Program")
    print('-'*30)

#show order summary
def order_summary():
    if not customer_order:
        print("\n🛒 Your order is empty.")
    else:
        print("\n======== Your Order Summary ========")
        total_price = sum(int(item["Price"][1:]) for item in customer_order)
        for idx, item in enumerate(customer_order, start=1):
            print(f"{idx}. {item['Name']} - {item['Price']}")
        print(f"\n💰 Total Price: ₱{total_price}")
        print("=====================================")

#remove order
def remove_item():

    if not customer_order:
        print("\n🛒 Your order is empty. Nothing to remove.")
        return
    
    order_summary()
    if customer_order:
        try:
            item_number = int(input("Enter the number of the item to remove: "))
            if 0 < item_number <= len(customer_order):
                removed_item = customer_order.pop(item_number - 1)
                print(f"❌ Removed {removed_item['Name']} from your order.")
            else:
                print("❌ Invalid item number.")
        except ValueError:
            print("❌ Invalid input. Please enter a number.")

#place order
def place_order():
    menu.print_menu()
    while True:
        try:
            tag = int(input("\nEnter (#) number of the item to add (0 to finish order): "))
            if tag == 0:
                print("Returning to main menu...\n")
                break

            item = menu.find_item(tag)
            if item:
                customer_order.append(item)
                print(f"✔ {item['Name']} added to your order.")
            else:
                print("❌ Invalid tag number. Please try again.")
        except ValueError:
            print("❌ Invalid input. Please enter a number.")

#finalizae order
def submit_order():
    if not customer_order:
        print("\n❌ You cannot submit an empty order.")
    else:
        order_summary()
        print("\n✅ Order submitted successfully!")
        customer_order.clear()

#options
while True:
    instructions()
    choice = input("Enter your choice: ").strip().lower()

    if choice == "s":
        menu.print_menu()
        input("Press 'Enter' to return to go back...")
    elif choice == "p":
        place_order()
    elif choice == "o":
        order_summary()
        input("Press 'Enter' to return to go back...")
    elif choice == "r":
        remove_item()
        break
    elif choice == "t":
        submit_order()
        break
    elif choice == "quit":
        print("👋 Thank you for using Quick Eats! Goodbye!")
        break
    else:
        print("❌ Invalid choice. Please try again.")
