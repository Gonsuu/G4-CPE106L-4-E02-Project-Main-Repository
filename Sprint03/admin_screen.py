from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import MDList, OneLineListItem
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from database import fetch_orders, update_order_status, delete_order 

class AdminScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orders = []

        self.layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        self.title = MDLabel(text="Admin Dashboard", halign="center", font_style="H5")
        self.layout.add_widget(self.title)

        self.scroll = ScrollView()
        self.list_view = MDList()
        self.scroll.add_widget(self.list_view)
        self.layout.add_widget(self.scroll)

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

        self.load_orders()

    def load_orders(self, *args):
        self.list_view.clear_widgets()
        self.orders = fetch_orders() 

        if not self.orders:
            self.list_view.add_widget(OneLineListItem(text="No pending orders."))
            return

        for order in self.orders:
            order_text = f"{order['customer_name']} - {order['item_name']} - ₱{order['price']} ({order['status']})"
            order_item = OneLineListItem(text=order_text, on_release=lambda x, o=order: self.show_order_options(o))
            self.list_view.add_widget(order_item)

    def show_order_options(self, order):
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
        update_order_status(order['order_id'], "Completed")
        dialog.dismiss()
        self.load_orders()

    def remove_order(self, order, dialog):
        delete_order(order['order_id'])
        dialog.dismiss()
        self.load_orders()

    def quit_program(self, instance):
        app = MDApp.get_running_app()
        app.stop()
