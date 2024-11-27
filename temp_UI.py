from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class DynamicInputApp(App):
    def build(self):
        # Main vertical layout
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # First line of input with a button to trigger dynamic input
        first_row = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
        self.input_field = TextInput(hint_text="Enter number of rows", multiline=False)
        add_rows_button = Button(text="Add Rows", on_press=self.add_rows)
        first_row.add_widget(Label(text="Rows:"))
        first_row.add_widget(self.input_field)
        first_row.add_widget(add_rows_button)

        # Add first row to layout
        self.layout.add_widget(first_row)

        # A sublayout for dynamically created rows
        self.dynamic_layout = BoxLayout(orientation='vertical', spacing=10)
        self.layout.add_widget(self.dynamic_layout)

        return self.layout

    def add_rows(self, instance):
        # Clear existing rows to prevent duplicates
        self.dynamic_layout.clear_widgets()

        # Get the number of rows to add from input_field
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

if __name__ == '__main__':
    DynamicInputApp().run()
