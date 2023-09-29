from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file("QuizPage.kv")


class QuizPageApp(App):
    def build(self):
        return QuizManager()


class QuizManager(ScreenManager):
    pass


class Question1Screen(Screen):
    def answer_question(self,is_correct):
        if is_correct:
            print("Correct")
            self.manager.current = "correct"
        else:
            self.manager.current = "error"


class Question2Screen(Screen):
    def check_answer(self, answer):
        if answer.lower() == "monkey":
            self.manager.current = "correct"
        else:
            self.manager.current = "error"


class CorrectScreen(Screen):
    def next_question(self):
        self.manager.current = "question2"


class ErrorScreen(Screen):
    pass


QuizPageApp().run()
