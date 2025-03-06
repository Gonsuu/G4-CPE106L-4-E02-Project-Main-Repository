from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.clock import Clock


class BillingScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = MDBoxLayout(orientation='vertical', spacing=20, padding=20)

        self.status_label = MDLabel(text="Select a billing option", halign="center")
        layout.add_widget(self.status_label)

        manual_billing_btn = MDRaisedButton(
            text="Manual Billing",
            on_release=self.process_manual_billing
        )
        layout.add_widget(manual_billing_btn)

        placeholder_btn = MDRaisedButton(
            text="Future Option (Coming Soon)"
        )
        layout.add_widget(placeholder_btn)

        self.add_widget(layout)

    def process_manual_billing(self, instance):
        self.status_label.text = "Manual Billing has been processed, please wait."
        Clock.schedule_once(self.reset_status, 3)

    def reset_status(self, dt):
        self.status_label.text = "Select a billing option"
