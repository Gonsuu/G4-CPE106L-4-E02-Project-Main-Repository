from modules.menu import Menu
from modules.order import Order

menu = Menu()
order = Order()

print("Menu:", menu.get_items())

order.add_order("Burger")
print("Your Orders:", order.get_orders())
