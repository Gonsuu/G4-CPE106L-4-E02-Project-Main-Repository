from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivy.uix.floatlayout import FloatLayout

class AdminScreen(Screen):
    def __init__(self, **kwargs):
        super(AdminScreen, self).__init__(**kwargs)

        layout = FloatLayout()

        title = MDLabel(
            text="Admin Screen",
            halign="center",
            size_hint=(None, None),
            height=50,
            width=200,
            pos_hint={'center_x': 0.5, 'top': 0.9}
        )
        layout.add_widget(title)

        check_orders_button = MDRaisedButton(
            text="Check Orders",
            size_hint=(None, None),
            height=50,
            width=200,
            pos_hint={'center_x': 0.5, 'top': 0.7},
            on_release=self.check_orders
        )
        layout.add_widget(check_orders_button)

        order_lists_button = MDRaisedButton(
            text="Order Lists",
            size_hint=(None, None),
            height=50,
            width=200,
            pos_hint={'center_x': 0.5, 'top': 0.6},
            on_release=self.order_lists
        )
        layout.add_widget(order_lists_button)

        quit_button = MDRaisedButton(
            text="Quit",
            size_hint=(None, None),
            height=50,
            width=200,
            pos_hint={'center_x': 0.5, 'top': 0.5},
            on_release=self.quit_program
        )
        layout.add_widget(quit_button)

        self.add_widget(layout)

    def check_orders(self, instance):
        # Implement the functionality to check orders
        print("Check Orders button clicked")

    def order_lists(self, instance):
        # Implement the functionality for order lists
        print("Order Lists button clicked")

    def quit_program(self, instance):
        # Quit the program
        app = MDApp.get_running_app()
        app.stop()
