import kivy
kivy.require('1.5.0')
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from database import DataBase


class Login(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(Login, self).__init__(**kwargs)
    
    def checkLoginInfo(self):
        if db.validate(self.username.text, self.password.text) == True:
            Profile.current = self.username.text
            self.username.text = ""
            self.password.text = ""
            sm.current = "prof"
        else:
            print("Incorrect Information")
    
class AccountCreation(Screen):
    given_name = ObjectProperty(None)
    username = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    re_enter_password = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(AccountCreation, self).__init__(**kwargs)

    def validName(self):
        if self.given_name.text == "":
            return False
        else:
            return True

    def validUsername(self):
        if self.username.text == "":
            return False
        else:
            return True
    
    def validEmail(self):
        if self.email.text == "":
            return False
        else:
            return True

    def validPassword(self):
        if self.password.text == "":
            return False
        else:
            return True

    def validRePass(self):
        if self.re_enter_password.text == self.password.text:
            return True
        else:
            print("Password must match")
            return False

    def clearInputs(self):
        self.given_name.text = ""
        self.username.text = ""
        self.email.text = ""
        self.password.text = ""
        self.re_enter_password.text = ""

    def validInfo(self):
        if self.validName() and self.validUsername() and self.validEmail() and self.validPassword() and self.validRePass() == True:
            db.add_user(self.username.text, self.given_name.text, self.email.text, self.password.text)
            self.clearInputs()
        else:
            print("Invalid Information")
    
    def backButton(self):
        self.clearInputs()
        self.manager.current = "login"
 
class Profile(Screen):
    username = ObjectProperty(None)
    n = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    current = ""
    
    def on_pre_enter(self, *args):
        n, email, password = db.get_user(self.current)
        self.username.text = "Account Name: " + self.current
        self.n.text = "Given Name: " + n
        self.email.text = "Email: " + email
        self.password.text = "Password: " + password

class WindowManager(ScreenManager):
    pass 

kv = Builder.load_file("log.kv")

sm = ScreenManager()
db = DataBase("data.txt")

screens = [Login(name="login"), AccountCreation(name="acct"), Profile(name="prof")]

for screen in screens:
    sm.add_widget(screen)

sm.current = "login"

class Login(App):
    def build(self):
        return sm

if __name__ == "__main__":
    Login().run()