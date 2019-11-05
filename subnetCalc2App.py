from kivy.app import App
from kivymd.uix.button import MDFlatButton
from kivymd.theming import ThemeManager
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

class Controller(BoxLayout):
    def btnPressed(self):
        print("pressed in controller")
        print(self.mytext)
        print(self.textfield_ipaddress.text)
    # theme_cls = ThemeManager()
    # mytext = ''

class subnetCalc2App(App):
    theme_cls = ThemeManager()
    mytext = ''

    def btnPressed(self):
        print("pressed in app")
        print(self.mytext)

    def build(self):
        return Controller()

subnetCalc2App().run()