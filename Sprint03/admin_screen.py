from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import MDList, OneLineListItem
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from database import fetch_orders, update_order_status, delete_order  # Import DB functions

class AdminScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orders = []  # Store current orders

        self.layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        # Title
        self.title = MDLabel(text="Admin Dashboard", halign="center", font_style="H5")
        self.layout.add_widget(self.title)

        # Scrollable Order List
        self.scroll = ScrollView()
        self.list_view = MDList()
        self.scroll.add_widget(self.list_view)
        self.layout.add_widget(self.scroll)

        # Action Buttons
        self.refresh_button = MDRaisedButton(
            text="Refresh Orders",
            pos_hint={"center_x": 0.5},
            on_release=self.load_orders
        )

        self.quit_button = MDRaisedButton(
            text="Quit",
            pos_hint={"center_x": 0.5},
            md_bg_color=(1, 0, 0, 1),
            on_release=self.quit_program
        )

        self.layout.add_widget(self.refresh_button)
        self.layout.add_widget(self.quit_button)
        self.add_widget(self.layout)

        self.load_orders()  # Load orders on screen initialization

    def load_orders(self, *args):
        """Fetch orders from the database and update the UI."""
        self.list_view.clear_widgets()  # Clear previous orders
        self.orders = fetch_orders()  # Fetch orders from DB

        if not self.orders:
            self.list_view.add_widget(OneLineListItem(text="No pending orders."))
            return

        for order in self.orders:
            order_text = f"{order['customer_name']} - {order['item_name']} - ₱{order['price']} ({order['status']})"
            order_item = OneLineListItem(text=order_text, on_release=lambda x, o=order: self.show_order_options(o))
            self.list_view.add_widget(order_item)

    def show_order_options(self, order):
        """Show dialog to update or remove an order."""
        dialog = MDDialog(
            title="Order Options",
            text=f"Customer: {order['customer_name']}\nItem: {order['item_name']}\nStatus: {order['status']}",
            buttons=[
                MDRaisedButton(text="Mark as Completed", on_release=lambda x: self.mark_as_completed(order, dialog)),
                MDRaisedButton(text="Remove Order", md_bg_color=(1, 0, 0, 1), on_release=lambda x: self.remove_order(order, dialog)),
                MDRaisedButton(text="Cancel", on_release=lambda x: dialog.dismiss())
            ]
        )
        dialog.open()

    def mark_as_completed(self, order, dialog):
        """Mark order as completed in the database."""
        update_order_status(order['order_id'], "Completed")
        dialog.dismiss()
        self.load_orders()

    def remove_order(self, order, dialog):
        """Remove an order from the database."""
        delete_order(order['order_id'])
        dialog.dismiss()
        self.load_orders()

    def quit_program(self, instance):
        # Quit the program
        app = MDApp.get_running_app()
        app.stop()
