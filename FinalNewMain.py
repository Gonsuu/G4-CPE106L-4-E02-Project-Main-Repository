# base modules
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel, MDIcon
from kivy.graphics import Color, Rectangle
from kivy.uix.image import Image
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.button import MDRaisedButton
from kivy.core.text import Label
import os

# local modules
from instructions_module import create_instructions
from Instructionscrap import create_instructions2
from helpers import customer_helper
from helpers import admin_helper
from menu_module import MenuScreen


class QuickEatsApp(MDApp):
    def build(self):
        self.screen = Screen()  # Assign the Screen object to self.screen

        #self.theme_cls.primary_palette = "Green"

        # Create top box for logo and app name using RelativeLayout
        top_box = RelativeLayout(
            size_hint=(1, 0.2),
            pos_hint={'center_x': 0.5, 'top': 1},
        )

        # Add the image
        logo = Image(
            source='C:/Users/itski/Desktop/Git-Projects/PythonProject/Image/QELogo.jpg',
            size_hint=(None, None),
            size=(300, 300),  # Adjust size as needed
            pos_hint={'center_x': 0.5, 'center_y': 0}  # Center horizontally
        )

        top_box.add_widget(logo)

        # Add the app name over the image
        #app_name = MDLabel(
            #text='Quick Eats',
            #halign='center',
            #theme_text_color="Custom",
            #text_color=(0.2, 0.1, 0, 1),  # Dark Brown color
            #font_name = 'Roboto-Italic',
            #font_style='H4',
            #size_hint=(1, None),
            #height = 50
        #)

        #top_box.add_widget(app_name)

        # Create button box for background of the buttons
        button_box = FloatLayout(
            size_hint=(1, 0.4),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}  # Centers the layout
        )

        self.admin_button = MDRaisedButton(
            text='Enter Admin', pos_hint={'center_x': 0.5, 'center_y': 0.6},
            on_release=self.enter_admin_role,
            theme_text_color="Custom",
            md_bg_color = 'white',
            text_color=(0.5, 0.25, 0, 1)  # Brown color
        )
        self.customer_button = MDRaisedButton(
            text='Enter Customer', pos_hint={'center_x': 0.5, 'center_y': 0.3},
            on_release=self.enter_customer_role,
            theme_text_color="Custom",
            md_bg_color='white',
            text_color=(0.5, 0.25, 0, 1)  # Brown color
        )

        self.Info_button = MDRaisedButton(
            text='Information', pos_hint={'center_x': 0.5, 'center_y': 0},
            on_release=self.enter_info_role,
            theme_text_color="Custom",
            md_bg_color='white',
            text_color=(0.5, 0.25, 0, 1)  # Brown color
        )

        button_box.add_widget(self.admin_button)
        button_box.add_widget(self.customer_button)
        button_box.add_widget(self.Info_button)

        # Add the boxes to the screen
        self.screen.add_widget(top_box)
        self.screen.add_widget(button_box)

        return self.screen

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def enter_admin_role(self, obj):
        self.enter_role(obj, role='admin')

    def enter_customer_role(self, obj):
        self.enter_role(obj, role='customer')

    def enter_info_role(self, obj):
        self.info_role(obj, role='information')

    def info_role(self, obj, role):
        self.screen.clear_widgets()
        # Insert group project information

    def enter_role(self, obj, role):
        self.screen.clear_widgets()

        if role == 'admin':
            self.username_layout = Builder.load_string(admin_helper)
        else:
            self.username_layout = Builder.load_string(customer_helper)

        self.screen.add_widget(self.username_layout)

        button = MDRaisedButton(
            text='Log in',
            pos_hint={'center_x': 0.5, 'center_y': 0.4},
            on_release=lambda x: self.show_data(x, role=role),
            theme_text_color="Custom",
            md_bg_color='white',
            text_color=(0.2, 0.1, 0, 1),
        )
        self.screen.add_widget(button)

    def show_data(self, obj, role):
        username_field = self.username_layout.ids.username
        if username_field.text == "":
            continue_button = MDRaisedButton(text='Continue',
                                             on_release=self.close_dialog,
                                             theme_text_color="Custom",
                                             md_bg_color = 'white',
                                             text_color=(0.2, 0.1, 0, 1)
                                             )
            check_string = 'Please enter a name'
            self.dialog = MDDialog(
                title='Welcome to Quick-Eats!',
                text=check_string,
                buttons=[continue_button],
                background_color=[1, 1, 1, 1]  # dialog background to white
            )
            self.dialog.open()
        elif role == 'admin' and self.username_layout.ids.password.text == "":
            continue_button = MDRaisedButton(text='Continue',
                                             on_release=self.close_dialog,
                                             theme_text_color="Custom",
                                             md_bg_color = 'white',
                                             text_color=(0.2, 0.1, 0, 1)
                                             )
            check_string = 'Please enter a password'
            self.dialog = MDDialog(
                title='Welcome to Quick-Eats!',
                text=check_string,
                buttons=[continue_button],
                background_color=[1, 1, 1, 1]  # dialog background to white
            )
            self.dialog.open()
        else:
            self.show_instructions(role)

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def show_instructions(self, role):
        username_field = self.username_layout.ids.username
        user_name = username_field.text

        handlers = {
            "S": self.show_menu,
            "P": self.place_order,
            "O": self.order_summary,
            "R": self.remove_item,
            "T": self.submit_order,
            "W": self.request_waiter,
            "quit": self.quit_program
        }

        instructions_layout = create_instructions2(user_name, role, handlers)

        self.screen.clear_widgets()  # Clear all widgets after continue
        self.screen.add_widget(instructions_layout)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.menu_screen = MenuScreen(self)  # Pass self (QuickEatsApp instance) to MenuScreen

    def show_menu(self, obj):
        self.screen.clear_widgets()  # Clear current screen
        self.screen.add_widget(self.menu_screen)  # Display the menu

    def place_order(self, obj):
        print("Place / Add an Order")

    def order_summary(self, obj):
        print("Order Summary")

    def remove_item(self, obj):
        print("Remove Item From Order")

    def submit_order(self, obj):
        print("Submit Your Order")

    def request_waiter(self, obj):
        print("Request Waiter for Manual Billing")

    def quit_program(self, obj):
        print("Quit The Program")
        return

QuickEatsApp().run()