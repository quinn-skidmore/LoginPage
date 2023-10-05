from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
Builder.load_file("LoginPage.kv")

accounts = {"quinn":"skidmore"}
special_characters = "`~!@#$%^&*()-_=+/\|][}{';:/.,?><"
numbers = "1234567890"


class LoginPageApp(App):
    def build(self):
        return LoginManager()


class LoginManager(ScreenManager):
    pass


class StartScreen(Screen):
    def create(self):
        self.manager.current = "create"

    def login(self):
        self.manager.current = "login"


class CreateScreen(Screen):
    def check_validity(self,username, password, password_confirm):
        special = False
        number = False
        capital = False
        lower = False
        if username not in accounts and password == password_confirm:
            for char in special_characters:
                if char in password:
                    special = True
            for num in numbers:
                if num in password:
                    number = True
            for char in password:
                if char.capitalize() == char:
                    capital = True
                if char.lower() == char:
                    lower = True

            if special and number and capital and lower and len(password) >= 8:
                accounts[username] = password
                self.manager.current = "welcome"
            else:
                print("incorrect")
                invalid = Label(text= "Invalid Password")
                self.ids.invalid.color = (1,0,0,1)
        pass

    def back(self):
        self.manager.current = "start"


class LoginScreen(Screen):
    def login(self, username, password):
        if username in accounts and accounts[username] == password:
            self.manager.current = "welcome"

    def back(self):
        self.manager.current = "start"
class WelcomeScreen(Screen):
    def sign_out(self):
        self.manager.current = "start"


LoginPageApp().run()
'''
Builder.load_file("QuizPage.kv")


class QuizPageApp(App):
    question_index = 1
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
    has_attempted = False
    def check_answer(self, answer):
        if answer.lower() == "monkey":
            self.manager.current = "correct"
        elif not self.has_attempted:
            self.ids.animlabel.color = (1,0,0,1)
            self.has_attempted = True
        else:
            self.ids.animlabel.color = (1, 1, 1, 1)
            self.manager.current = "error"
            self.has_attempted = False



class CorrectScreen(Screen):
    def next_question(self):
        QuizPageApp.question_index += 1
        self.manager.current = "question" + str(QuizPageApp.question_index)


class ErrorScreen(Screen):
    def retry_quiz(self):
        self.manager.current = "question1"
        QuizPageApp.question_index = 1


QuizPageApp().run()
'''