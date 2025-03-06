# base modules
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivy.uix.image import Image
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.button import MDRaisedButton

# local modules
from Instructionscrap import create_instructions2
from helpers import customer_helper
from helpers import admin_helper
from menu_module import MenuScreen
from selected_item_screen import SelectedItemScreen
from order_summary_screen import OrderSummaryScreen
from remove_item_screen import RemoveItemFromOrder
from submit_order_screen import SubmitOrderScreen
from billing_screen import BillingScreen
from admin_screen import AdminScreen  # Import the AdminScreen

class QuickEatsApp(MDApp):
    def build(self):
        self.screen_manager = ScreenManager()

        self.main_screen = Screen(name="main")
        self.menu_screen = MenuScreen(name="menu")
        self.selected_item_screen = SelectedItemScreen(name="selected_item")
        self.order_summary_screen = OrderSummaryScreen(name="order_summary")
        self.remove_item_screen = RemoveItemFromOrder(name="remove_item")
        self.submit_order_screen = SubmitOrderScreen(name="submit_order")
        self.billing_screen = BillingScreen(name="billing")
        self.admin_screen = AdminScreen(name="admin")  # Create the AdminScreen

        self.screen_manager.add_widget(self.main_screen)
        self.screen_manager.add_widget(self.menu_screen)
        self.screen_manager.add_widget(self.selected_item_screen)
        self.screen_manager.add_widget(self.order_summary_screen)
        self.screen_manager.add_widget(self.remove_item_screen)
        self.screen_manager.add_widget(self.submit_order_screen)
        self.screen_manager.add_widget(self.billing_screen)
        self.screen_manager.add_widget(self.admin_screen)  # Add the AdminScreen to the manager

        self.init_main_screen()

        return self.screen_manager

    def init_main_screen(self):
        # Create top box for logo and app name
        top_box = RelativeLayout(
            size_hint=(1, 0.2),
            pos_hint={'center_x': 0.5, 'top': 1},
        )

        # Add the image
        logo = Image(
            source='C:/Users/itski/Desktop/Git-Projects/PythonProject/Image/QELogo.jpg',
            size_hint=(None, None),
            size=(300, 300),
            pos_hint={'center_x': 0.5, 'center_y': 0}
        )

        top_box.add_widget(logo)

        # Store button_box as an instance variable
        self.button_box = FloatLayout(
            size_hint=(1, 0.4),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )

        self.admin_button = MDRaisedButton(
            text='Enter Admin', pos_hint={'center_x': 0.5, 'center_y': 0.6},
            on_release=self.enter_admin_role,
            theme_text_color="Custom",
            md_bg_color='white',
            text_color=(0.5, 0.25, 0, 1)
        )
        self.customer_button = MDRaisedButton(
            text='Enter Customer', pos_hint={'center_x': 0.5, 'center_y': 0.3},
            on_release=self.enter_customer_role,
            theme_text_color="Custom",
            md_bg_color='white',
            text_color=(0.5, 0.25, 0, 1)
        )

        self.info_button = MDRaisedButton(
            text='Information', pos_hint={'center_x': 0.5, 'center_y': 0},
            on_release=self.enter_info_role,
            theme_text_color="Custom",
            md_bg_color='white',
            text_color=(0.5, 0.25, 0, 1)
        )

        # Add buttons to button_box
        self.button_box.add_widget(self.admin_button)
        self.button_box.add_widget(self.customer_button)
        self.button_box.add_widget(self.info_button)

        # Add to main screen
        self.main_screen.add_widget(top_box)
        self.main_screen.add_widget(self.button_box)

    def enter_admin_role(self, obj):
        self.enter_role(obj, role='admin')

    def enter_customer_role(self, obj):
        self.enter_role(obj, role='customer')

    def enter_info_role(self, obj):
        self.info_role(obj, role='information')

    def info_role(self, obj, role):
        self.main_screen.clear_widgets()
        # Insert group project information

    def enter_role(self, obj, role):
        self.main_screen.clear_widgets()

        if role == 'admin':
            self.username_layout = Builder.load_string(admin_helper)
        else:
            self.username_layout = Builder.load_string(customer_helper)

        self.main_screen.add_widget(self.username_layout)

        button = MDRaisedButton(
            text='Log in',
            pos_hint={'center_x': 0.5, 'center_y': 0.2},
            on_release=lambda x: self.show_data(x, role=role),
            theme_text_color="Custom",
            md_bg_color='white',
            text_color=(0.2, 0.1, 0, 1),
        )
        self.main_screen.add_widget(button)

    def show_data(self, obj, role):
        if hasattr(self, "username_layout") and hasattr(self.username_layout, "ids"):
            username_field = self.username_layout.ids.get("username")
            password_field = self.username_layout.ids.get("password")

            if not username_field:
                self.show_error_dialog('Username field not found!')
                return

            if role == "admin" and not password_field:
                self.show_error_dialog('Password field not found!')
                return

            if username_field.text == "":
                self.show_error_dialog('Please enter a name')
            elif role == 'admin' and password_field.text == "":
                self.show_error_dialog('Please enter a password')
            elif role == 'admin' and (username_field.text != "root" or password_field.text != "root123"):
                self.show_error_dialog('Invalid username or password')
            else:
                self.show_instructions(role)
        else:
            print("Error: username_layout or ids not found!")

    def show_error_dialog(self, message):
        continue_button = MDRaisedButton(
            text='Continue',
            on_release=self.close_dialog,
            theme_text_color="Custom",
            md_bg_color='white',
            text_color=(0.2, 0.1, 0, 1)
        )
        self.dialog = MDDialog(
            title='Error',
            text=message,
            buttons=[continue_button],
            background_color=[1, 1, 1, 1]  # dialog background to white
        )
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def show_instructions(self, role):
        if role == 'admin':
            self.screen_manager.current = 'admin'
        else:
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

            self.main_screen.clear_widgets()  # Clear all widgets after continue
            self.main_screen.add_widget(instructions_layout)

    def show_menu(self, obj):
        self.screen_manager.current = "menu"  # Switch to menu screen

    def place_order(self, obj):
        self.screen_manager.current = "menu"  # Switch to menu screen

    def order_summary(self, obj):
        if not self.order_summary_screen.orders:
            dialog = MDDialog(
                title="Order Summary",
                text="There are no orders listed.",
                buttons=[
                    MDRaisedButton(text="OK",
                                   on_release=lambda x: dialog.dismiss()
                                   )
                ]
            )
            dialog.open()
        else:
            self.screen_manager.current = "order_summary"

    def remove_item(self, obj):
        self.screen_manager.current = "remove_item"

    def submit_order(self, obj):
        if not self.submit_order_screen.set_orders(self.order_summary_screen.orders):
            dialog = MDDialog(
                title="Submit Order",
                text="There are no orders listed.",
                buttons=[
                    MDRaisedButton(text="OK",
                                   on_release=lambda x: dialog.dismiss()
                                   )
                ]
            )
            dialog.open()
        else:
            self.screen_manager.current = "submit_order"

    def request_waiter(self, obj):
        print("Request Waiter for Manual Billing has been processed, please wait.")

        if not self.billing_screen:
            dialog = MDDialog(
                title="Order Summary",
                text="There are no orders listed.",
                buttons=[
                    MDRaisedButton(text="OK",
                                   on_release=lambda x: dialog.dismiss()
                                   )
                ]
            )
            dialog.open()
        else:
            self.screen_manager.current = "billing"

    def quit_program(self, obj):
        print("Quit The Program")
        self.stop()


QuickEatsApp().run()
