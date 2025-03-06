from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock


class BillingScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Create a FloatLayout for flexible positioning
        layout = FloatLayout()

        # Status label - Centered on the screen
        self.status_label = MDLabel(
            text="Select a billing option",
            halign="center",
            size_hint=(None, None),
            width=300,  # Prevents text wrapping
            pos_hint={"center_x": 0.5, "center_y": 0.7},  # Centering the label higher
            font_style="H5"
        )
        layout.add_widget(self.status_label)

        # QR Code Image (Initially hidden)
        self.qr_image = Image(
            source="C:/Users/itski/Desktop/Git-Projects/PythonProject/Image/GCashQR.jpg",
            size_hint=(None, None),
            size=(500, 500),  # Adjust as needed
            pos_hint={"center_x": 0.5, "center_y": 0.6},  # Positioned at the center
            opacity=0  # Hidden by default
        )
        layout.add_widget(self.qr_image)

        # BoxLayout for buttons (positioned lower)
        self.button_box = BoxLayout(
            orientation="vertical",
            spacing=20,
            size_hint=(0.8, 0.3),  # Adjust button container size
            pos_hint={"center_x": 0.43, "y": 0.1}  # Lowering the button box
        )

        # Buttons
        self.manual_billing_btn = MDRaisedButton(
            text="Manual Billing",
            on_release=self.process_manual_billing
        )
        self.digital_payment_btn = MDRaisedButton(
            text="Digital Payment",
            on_release=self.show_qr_code
        )
        self.return_button = MDRaisedButton(
            text="Return",
            on_release=self.return_to_main
        )

        # Add buttons in the correct order
        self.button_box.add_widget(self.manual_billing_btn)
        self.button_box.add_widget(self.digital_payment_btn)
        self.button_box.add_widget(self.return_button)

        layout.add_widget(self.button_box)
        self.add_widget(layout)

    def process_manual_billing(self, instance):
        self.status_label.text = "Manual Billing has been processed, please wait."
        Clock.schedule_once(self.reset_status, 3)

    def show_qr_code(self, instance):
        """Display the QR code and remove Manual Billing button."""
        self.qr_image.opacity = 1  # Show QR code
        if self.manual_billing_btn in self.button_box.children:
            self.button_box.remove_widget(self.manual_billing_btn)  # Remove manual billing button

    def return_to_main(self, instance):
        """Restore original button order when returning."""
        self.qr_image.opacity = 0  # Hide QR code

        # Clear the button box and re-add widgets in the correct order
        self.button_box.clear_widgets()

        self.button_box.add_widget(self.manual_billing_btn)  # Manual Billing at the top
        self.button_box.add_widget(self.digital_payment_btn)  # Digital Payment in the middle
        self.button_box.add_widget(self.return_button)  # Return at the bottom

        self.manager.current = "main"  # Go back to main screen

    def reset_status(self, dt):
        self.status_label.text = "Select a billing option"
