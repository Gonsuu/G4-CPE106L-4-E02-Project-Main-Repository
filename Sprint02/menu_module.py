from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDRaisedButton
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label

class MenuScreen(Screen):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app  # Reference to main app
        self.food_items = ["Burger", "Pizza", "Pasta", "Salad", "Sushi"]
        self.cart = {item: 0 for item in self.food_items}  # Track order quantities
        self.build_menu()

    def build_menu(self):
        # **Main container (vertical)**
        main_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        # **Scrollable Menu**
        scroll_view = ScrollView(size_hint=(1, 0.8))  # 80% height for menu
        self.menu_list = BoxLayout(orientation="vertical", size_hint_y=None)
        self.menu_list.bind(minimum_height=self.menu_list.setter("height"))

        # **Add food items**
        for item in self.food_items:
            self.add_food_item(item)

        scroll_view.add_widget(self.menu_list)
        main_layout.add_widget(scroll_view)

        # **Buttons for Order**
        btn_layout = BoxLayout(size_hint_y=None, height=50, spacing=10)
        btn_place_order = MDRaisedButton(text="Place Order", on_release=self.place_order)
        btn_remove_order = MDRaisedButton(text="Remove Order", on_release=self.remove_order)

        btn_layout.add_widget(btn_place_order)
        btn_layout.add_widget(btn_remove_order)
        main_layout.add_widget(btn_layout)

        self.add_widget(main_layout)

    def add_food_item(self, item):
        """ Adds a food item to the menu list with (+) and (-) buttons """
        food_layout = BoxLayout(orientation="horizontal", size_hint_y=None, height=50, spacing=10)

        # Food item label
        food_label = Label(text=f"{item} (0)", size_hint_x=0.6)

        # (-) Button
        btn_decrease = MDRaisedButton(
            text="-",
            size_hint_x=None, width=40,
            on_release=lambda instance: self.update_quantity(item, -1, food_label)
        )

        # (+) Button
        btn_increase = MDRaisedButton(
            text="+",
            size_hint_x=None, width=40,
            on_release=lambda instance: self.update_quantity(item, 1, food_label)
        )

        food_layout.add_widget(food_label)
        food_layout.add_widget(btn_decrease)
        food_layout.add_widget(btn_increase)

        self.menu_list.add_widget(food_layout)  # Add to scrollable list

    def update_quantity(self, item, change, food_label):
        """ Updates the quantity of an item and updates the label """
        self.cart[item] += change
        self.cart[item] = max(0, self.cart[item])  # Prevent negative values
        food_label.text = f"{item} ({self.cart[item]})"  # Update label text

    def place_order(self, instance):
        print("Placing order:", self.cart)

    def remove_order(self, instance):
        print("Removing order:", self.cart)
