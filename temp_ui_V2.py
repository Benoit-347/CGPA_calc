from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen

class InputWindow(Screen):
    def __init__(self, screen_manager, window_id, **kwargs):
        super().__init__(**kwargs)
        self.screen_manager = screen_manager
        self.window_id = window_id

        # Main layout
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        self.add_widget(self.layout)

        # First row: Input field and button
        first_row = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
        self.input_field = TextInput(hint_text="Enter number of rows", multiline=False)
        add_rows_button = Button(text="Add Rows", on_press=self.add_rows)
        first_row.add_widget(Label(text=f"Window {window_id}: Rows"))
        first_row.add_widget(self.input_field)
        first_row.add_widget(add_rows_button)

        self.layout.add_widget(first_row)

        # Sub-layout for dynamically added rows
        self.dynamic_layout = BoxLayout(orientation='vertical', spacing=10)
        self.layout.add_widget(self.dynamic_layout)

        # Next window button
        self.next_button = Button(text="Next Window", size_hint_y=None, height=40, on_press=self.next_window)
        self.next_button.disabled = True  # Initially disabled
        self.layout.add_widget(self.next_button)

    def add_rows(self, instance):
        # Clear existing rows
        self.dynamic_layout.clear_widgets()

        # Get number of rows
        try:
            num_rows = int(self.input_field.text)
            if num_rows < 1:
                raise ValueError("Number of rows must be >= 1")
        except ValueError:
            self.input_field.text = "Invalid input"
            return

        # Add rows dynamically
        for i in range(num_rows):
            row = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
            row.add_widget(Label(text=f"Row {i + 1}:"))
            row.add_widget(TextInput(hint_text=f"Input {i + 1}"))
            self.dynamic_layout.add_widget(row)

        # Enable the Next Window button
        self.next_button.disabled = False

    def next_window(self, instance):
        # Create the next window dynamically
        next_window_id = self.window_id + 1
        next_window = InputWindow(self.screen_manager, next_window_id, name=f"window_{next_window_id}")
        self.screen_manager.add_widget(next_window)
        self.screen_manager.current = f"window_{next_window_id}"


class DynamicInputApp(App):
    def build(self):
        # Create the ScreenManager
        self.screen_manager = ScreenManager()

        # Add the first window
        first_window = InputWindow(self.screen_manager, window_id=1, name="window_1")
        self.screen_manager.add_widget(first_window)

        return self.screen_manager


if __name__ == '__main__':
    DynamicInputApp().run()
