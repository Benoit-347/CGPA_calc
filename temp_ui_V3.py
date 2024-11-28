from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen

class InputWindow(Screen):
    def __init__(self, window_id, total_windows, **kwargs):
        super().__init__(**kwargs)
        self.window_id = window_id
        self.total_windows = total_windows

        # Main layout
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        self.add_widget(self.layout)

        # First row: Input field and button
        first_row = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
        self.input_field = TextInput(hint_text="Enter number of rows", multiline=False)
        add_rows_button = Button(text="Add Rows", on_press=self.add_rows)
        first_row.add_widget(Label(text=f"Window {window_id}/{total_windows}: Rows"))
        first_row.add_widget(self.input_field)
        first_row.add_widget(add_rows_button)

        self.layout.add_widget(first_row)

        # Sub-layout for dynamically added rows
        self.dynamic_layout = BoxLayout(orientation='vertical', spacing=10)
        self.layout.add_widget(self.dynamic_layout)

        # Navigation buttons
        nav_buttons = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
        self.prev_button = Button(text="Previous", size_hint_x=0.5, on_press=self.previous_window)
        self.next_button = Button(text="Next", size_hint_x=0.5, on_press=self.next_window)
        nav_buttons.add_widget(self.prev_button)
        nav_buttons.add_widget(self.next_button)

        self.layout.add_widget(nav_buttons)

        # Disable navigation buttons if not applicable
        self.update_nav_buttons()

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

    def next_window(self, instance):
        # Navigate to the next screen
        if self.window_id < self.total_windows:
            self.manager.current = f"window_{self.window_id + 1}"

    def previous_window(self, instance):
        # Navigate to the previous screen
        if self.window_id > 1:
            self.manager.current = f"window_{self.window_id - 1}"

    def update_nav_buttons(self):
        # Disable/Enable navigation buttons based on current window
        self.prev_button.disabled = (self.window_id == 1)
        self.next_button.disabled = (self.window_id == self.total_windows)


class DynamicInputApp(App):
    def __init__(self, total_windows=3, **kwargs):
        super().__init__(**kwargs)
        self.total_windows = total_windows

    def build(self):
        # Create the ScreenManager
        self.screen_manager = ScreenManager()

        # Create predetermined windows
        for i in range(1, self.total_windows + 1):
            window = InputWindow(window_id=i, total_windows=self.total_windows, name=f"window_{i}")
            self.screen_manager.add_widget(window)

        # Set the initial screen
        self.screen_manager.current = "window_1"

        return self.screen_manager


if __name__ == '__main__':
    # Number of windows is predetermined here
    DynamicInputApp(total_windows=5).run()
