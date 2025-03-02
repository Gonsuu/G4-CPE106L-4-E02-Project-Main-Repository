from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivy.uix.image import Image

class SelectedItemScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        self.image = Image(size_hint=(1, 0.5))
        self.item_name = MDLabel(text="Item Name", halign="center", font_style="H5")
        self.item_price = MDLabel(text="Price", halign="center", font_style="H6")

        self.layout.add_widget(self.image)
        self.layout.add_widget(self.item_name)
        self.layout.add_widget(self.item_price)

        self.return_button = MDRaisedButton(
            text="Back to Menu",
            pos_hint={"center_x": 0.5},
            on_release=self.go_back,
            md_bg_color='white',
            text_color=(0.5, 0.25, 0, 1)
        )

        self.layout.add_widget(self.return_button)
        self.add_widget(self.layout)

    def update_item(self, item):
        self.item_name.text = item["name"]
        self.item_price.text = f"Price: {item['price']}"
        self.image.source = "C:/Users/itski/Desktop/Git-Projects/PythonProject/Image/QELogo.jpg"

    def go_back(self, instance):
        self.manager.current = "menu"
