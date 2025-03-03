from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.list import MDList, OneLineListItem
from kivy.uix.scrollview import ScrollView
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel

class OrderSummaryScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orders = []

        self.layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        self.title = MDLabel(text="Order Summary", halign="center", font_style="H5")
        self.layout.add_widget(self.title)

        self.scroll = ScrollView()
        self.list_view = MDList()
        self.scroll.add_widget(self.list_view)

        self.layout.add_widget(self.scroll)

        self.checkout_button = MDRaisedButton(
            text="Submit Order",
            pos_hint={"center_x": 0.5},
            md_bg_color=(0.2, 0.6, 0.2, 1),
        )

        self.return_button = MDRaisedButton(
            text="Back",
            pos_hint={"center_x": 0.5},
            on_release=self.return_to_main
        )

        self.layout.add_widget(self.checkout_button)
        self.layout.add_widget(self.return_button)
        self.add_widget(self.layout)

    def add_item_to_order(self, item):
        self.orders.append(item)
        order_item = OneLineListItem(text=f"{item['name']} - {item['price']}")
        self.list_view.add_widget(order_item)

    def remove_selected_item(self, item):
        if item in self.order:
            self.order.remove(item)
            self.update_order(self.order)

    def return_to_main(self, instance):
        self.manager.current = 'main'
