import csv
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

# Define subjects and credits
subjects = ['Math', 'Chemistry', 'PLC', 'CAED', 'Civil', 'English', 'SFH', 'Kannada']
credits = [4, 4, 3, 3, 3, 1, 1, 1]

# Data structure to store inputs
all_data = {}


class SubjectRow(BoxLayout):
    def __init__(self, subject, credit, **kwargs):
        super().__init__(orientation='horizontal', spacing=10, **kwargs)
        self.subject = subject

        # Subject Label
        self.add_widget(Label(text=subject, size_hint=(0.2, 1)))

        # Assignment Marks
        self.assignment_input = TextInput(hint_text="Assignment Mark (out of 10)", multiline=False)
        self.add_widget(self.assignment_input)

        # Lab Marks
        self.lab_input = TextInput(hint_text="Lab Mark (out of 30)", multiline=False)
        self.add_widget(self.lab_input)

        # IA Marks
        self.ia_input = TextInput(hint_text="IA Mark (out of 50)", multiline=False)
        self.add_widget(self.ia_input)

        # Credit Weight (default shown)
        self.credit_input = TextInput(text=str(credit), multiline=False)
        self.add_widget(self.credit_input)

    def get_data(self):
        try:
            assignment = float(self.assignment_input.text)
            lab = float(self.lab_input.text)
            ia = float(self.ia_input.text)
            credit = int(self.credit_input.text)
            return {'assignment': assignment, 'lab': lab, 'IA': ia, 'credit': credit}
        except ValueError:
            return None  # Handle invalid inputs later


class CGPAApp(App):
    def build(self):
        self.root = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Scrollable area for subject rows
        scroll_view = ScrollView(size_hint=(1, 0.7))
        self.grid = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.grid.bind(minimum_height=self.grid.setter('height'))
        scroll_view.add_widget(self.grid)

        # Add rows for each subject
        self.subject_rows = []
        for subject, credit in zip(subjects, credits):
            row = SubjectRow(subject, credit)
            self.subject_rows.append(row)
            self.grid.add_widget(row)

        self.root.add_widget(scroll_view)

        # Buttons for actions
        button_layout = BoxLayout(size_hint=(1, 0.2), spacing=10)

        calc_button = Button(text="Calculate CGPA")
        calc_button.bind(on_press=self.calculate_cgpa)
        button_layout.add_widget(calc_button)

        predict_button = Button(text="Predict Marks")
        predict_button.bind(on_press=self.predict_marks)
        button_layout.add_widget(predict_button)

        self.root.add_widget(button_layout)
        return self.root

    def collect_data(self):
        """Collect data from all rows."""
        global all_data
        all_data = {}
        for row in self.subject_rows:
            data = row.get_data()
            if data:
                all_data[row.subject] = data
            else:
                self.show_error("Invalid input detected. Please correct all fields.")
                return None
        return all_data

    def calculate_cgpa(self, instance):
        if self.collect_data():
            cgpa = self.calc_CGPA_sem()
            self.show_popup("CGPA Result", f"Your Semester CGPA is: {cgpa:.2f}")

    def predict_marks(self, instance):
        if self.collect_data():
            req_cgpa = self.prompt_user("Enter required CGPA:")
            if req_cgpa:
                req_cgpa = float(req_cgpa)
                ia_left = self.prompt_user("Enter IAs left:")
                if ia_left:
                    ia_left = int(ia_left)
                    external_expected = self.prompt_user("Expected external marks:")
                    if external_expected:
                        external_expected = float(external_expected)
                        predictions = self.predict(req_cgpa, ia_left, external_expected)
                        result = "\n".join([f"{sub}: {marks}" for sub, marks in predictions])
                        self.show_popup("Prediction Result", f"Marks Required per Subject:\n\n{result}")

    def show_error(self, message):
        """Show error popup."""
        popup = Popup(title="Error", content=Label(text=message), size_hint=(0.8, 0.4))
        popup.open()

    def show_popup(self, title, message):
        """Show popup for results."""
        popup = Popup(title=title, content=Label(text=message), size_hint=(0.8, 0.4))
        popup.open()

    def prompt_user(self, message):
        """Prompt user for input."""
        popup_layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        input_field = TextInput(multiline=False, size_hint=(1, 0.7))
        popup_layout.add_widget(Label(text=message))
        popup_layout.add_widget(input_field)

        submit_button = Button(text="Submit", size_hint=(1, 0.3))
        popup_layout.add_widget(submit_button)

        popup = Popup(title="Input Required", content=popup_layout, size_hint=(0.8, 0.5))
        result = {}

        def on_submit(instance):
            result['value'] = input_field.text
            popup.dismiss()

        submit_button.bind(on_press=on_submit)
        popup.open()
        popup.bind(on_dismiss=lambda instance: result.setdefault('value', None))
        return result.get('value')

    def calc_CGPA_sem(self):
        """Calculate CGPA for the semester."""
        total_marks, total_credits = 0, 0
        for subject, data in all_data.items():
            total_marks += data['assignment'] + data['lab'] + data['IA']
            total_credits += data['credit']
        return total_marks / total_credits if total_credits else 0

    def predict(self, req_cgpa, ia_left, external_expected):
        """Predict marks required to achieve a target CGPA."""
        predictions = []
        for subject, data in all_data.items():
            current_marks = data['assignment'] + data['lab'] + data['IA']
            required_marks = (req_cgpa * (current_marks + ia_left) - external_expected) / ia_left
            predictions.append((subject, required_marks))
        return predictions


if __name__ == '__main__':
    CGPAApp().run()
