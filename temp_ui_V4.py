from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen

class SubjectScreen(Screen):
    def __init__(self, subject, index, total_subjects, result_list, **kwargs):
        super().__init__(**kwargs)
        self.subject = subject
        self.index = index
        self.total_subjects = total_subjects
        self.result_list = result_list

        # Layout
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout.add_widget(Label(text=f"{subject}™ Window", font_size=24))

        # Inputs
        self.assignment_input = TextInput(hint_text="Enter Assignment Mark", multiline=False)
        self.lab_input = TextInput(hint_text="Enter Lab Mark", multiline=False)
        self.ia_input = TextInput(hint_text="Enter IA Mark", multiline=False)

        layout.add_widget(Label(text="Assignment Mark:"))
        layout.add_widget(self.assignment_input)

        layout.add_widget(Label(text="Lab Mark:"))
        layout.add_widget(self.lab_input)

        layout.add_widget(Label(text="IA Mark:"))
        layout.add_widget(self.ia_input)

        # Navigation button
        self.next_button = Button(text="Next", on_press=self.collect_and_continue)
        layout.add_widget(self.next_button)

        self.add_widget(layout)

    def collect_and_continue(self, instance):
        # Collect data from inputs
        ans = [
            self.assignment_input.text,
            self.lab_input.text,
            self.ia_input.text
        ]
        self.result_list.append(ans)

        # Navigate to the next screen
        if self.index < self.total_subjects - 1:
            self.manager.current = f"subject_{self.index + 1}"
        else:
            self.manager.current = "result_screen"


class ResultScreen(Screen):
    def __init__(self, result_list, subject_list, **kwargs):
        super().__init__(**kwargs)
        self.result_list = result_list
        self.subject_list = subject_list

        # Layout
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout.add_widget(Label(text="Results", font_size=24))

        # Display results
        for i, subject in enumerate(subject_list):
            layout.add_widget(Label(text=f"{subject}: {self.result_list[i]}"))

        # Add a finish button
        finish_button = Button(text="Finish", on_press=self.finish)
        layout.add_widget(finish_button)

        self.add_widget(layout)

    def finish(self, instance):
        App.get_running_app().stop()


class SubjectInputApp(App):
    def build(self):
        # Data
        subject_list = ['math', 'chemistry', 'plc']
        result_list = []

        # Create ScreenManager
        sm = ScreenManager()

        # Add Subject Screens
        for i, subject in enumerate(subject_list):
            screen = SubjectScreen(
                subject=subject,
                index=i,
                total_subjects=len(subject_list),
                result_list=result_list,
                name=f"subject_{i}"
            )
            sm.add_widget(screen)

        # Add Result Screen
        result_screen = ResultScreen(result_list=result_list, subject_list=subject_list, name="result_screen")
        sm.add_widget(result_screen)

        # Set the first screen
        sm.current = "subject_0"

        return sm


if __name__ == '__main__':
    SubjectInputApp().run()
