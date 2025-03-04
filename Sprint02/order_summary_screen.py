from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import MDList, OneLineListItem
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from database import insert_order  # Import the database function

class OrderSummaryScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orders = []  # Store current orders

        self.layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        self.title = MDLabel(text="Order Summary", halign="center", font_style="H5")
        self.layout.add_widget(self.title)

        self.scroll = ScrollView()
        self.list_view = MDList()
        self.scroll.add_widget(self.list_view)
        self.layout.add_widget(self.scroll)

        self.submit_button = MDRaisedButton(
            text="Submit Order",
            pos_hint={"center_x": 0.5},
            md_bg_color=(0.2, 0.6, 0.2, 1),
            on_release=self.submit_order
        )

        self.return_button = MDRaisedButton(
            text="Back",
            pos_hint={"center_x": 0.5},
            on_release=self.return_to_main
        )

        self.layout.add_widget(self.submit_button)
        self.layout.add_widget(self.return_button)
        self.add_widget(self.layout)

    def set_orders(self, orders):
        """Set the orders list and update the UI."""
        self.orders = orders
        self.update_order_list()

    def add_item_to_order(self, item):
        """Add a new item to the order list and update UI."""
        self.orders.append(item)
        self.update_order_list()

    def update_order_list(self):
        """Refresh UI to display orders."""
        self.list_view.clear_widgets()
        for item in self.orders:
            order_item = OneLineListItem(text=f"{item['name']} - {item['price']}")
            self.list_view.add_widget(order_item)

    def submit_order(self, instance):
        """Send orders to database and go to Submit Order Screen."""
        if not self.orders:
            dialog = MDDialog(
                title="Error",
                text="No orders to submit.",
                buttons=[MDRaisedButton(text="OK", on_release=lambda x: dialog.dismiss())]
            )
            dialog.open()
            return

        for item in self.orders:
            insert_order(item["name"], item["price"])  # Send order to DB

        dialog = MDDialog(
            title="Success",
            text="Order submitted successfully!",
            buttons=[MDRaisedButton(text="OK", on_release=lambda x: dialog.dismiss())]
        )
        dialog.open()

        self.orders.clear()  # Clear orders after submission
        self.update_order_list()  # Refresh UI

        self.manager.current = "submit_order"  # Switch to next screen

    def return_to_main(self, instance):
        self.manager.current = "main"
