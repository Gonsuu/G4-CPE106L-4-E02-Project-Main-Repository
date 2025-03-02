from kivymd.uix.label import MDLabel
from kivy.uix.boxlayout import BoxLayout

def create_instructions(user_name, role):

    instructions_text = (
        '-' * 30 + '\n' + #Turn all options/choices into buttons
        f"Welcome to Quick-Eats, {user_name}!\n" +
        '-' * 30 + '\n' +
        "S : Show Menu\n" +
        "P : Place / Add an Order\n" +
        "O : Order Summary\n" +
        "R : Remove Item From Order\n" +
        "T : Submit Your Order\n" +
        "W : Request Waiter for Manual Billing\n" +
        "quit : Quit The Program\n" +
        '-' * 30
    )

    instructions_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
    instructions = MDLabel(
        text=instructions_text,
        halign="center",
        theme_text_color="Primary"
    )
    instructions_layout.add_widget(instructions)
    return instructions_layout