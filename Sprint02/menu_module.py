from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.uix.list import ThreeLineAvatarIconListItem, ImageLeftWidget, MDList
from kivymd.uix.button import MDRaisedButton
from kivy.graphics import Color, RoundedRectangle
from menu import Menu

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #Create a Menu instance
        self.menu = Menu()

        # Correct path to the logo
        logo_path = r"C:/Users/itski/Desktop/Git-Projects/PythonProject/Image/QELogo.jpg"

        # Create the main layout (vertical)
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Add a logo/image at the top
        logo = Image(source=logo_path, size_hint=(1, 0.2), allow_stretch=False, keep_ratio=False)
        main_layout.add_widget(logo)

        # Create a centered menu layout
        menu_container = AnchorLayout(size_hint=(1, 0.6))

        # Create a box layout for the menu list with a red background and rounded edges
        menu_box = BoxLayout(
            orientation='vertical',
            size_hint=(0.9, 0.9),
            height=400,
            pos_hint={'center_y': 0.8}
        )
        with menu_box.canvas.before:
            Color(0, 0, 0, 0)
            self.rect = RoundedRectangle(size=menu_box.size, pos=menu_box.pos, radius=[20])
        menu_box.bind(size=self._update_rect, pos=self._update_rect)

        # Create a scroll view for the menu list
        scroll = ScrollView()
        list_view = MDList()
        scroll.add_widget(list_view)

        #Get menu items and add them
        for item in self.menu.get_menu_items():
            item_image = ImageLeftWidget(source=logo_path)
            menu_item = ThreeLineAvatarIconListItem(
                text=item["name"],
                secondary_text=f"Price: {item['price']}",
                tertiary_text=f"Tag: {item['tag']}"
            )
            menu_item.add_widget(item_image)
            list_view.add_widget(menu_item)

        # Add scroll view to the menu box
        menu_box.add_widget(scroll)

        # Add menu box to the container
        menu_container.add_widget(menu_box)

        # Create a return button
        return_button = MDRaisedButton(
            text='Return',
            size_hint=(None, None),
            size=(100, 50),
            pos_hint={'center_x': 0.5},
            on_release=self.return_to_main,
            theme_text_color="Custom",
            md_bg_color='white',
            text_color=(0.5, 0.25, 0, 1)
        )

        # Add everything to the main layout
        main_layout.add_widget(menu_container)
        main_layout.add_widget(return_button)

        # Add the main layout to the screen
        self.add_widget(main_layout)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def return_to_main(self, instance):
        self.manager.current = 'main'
