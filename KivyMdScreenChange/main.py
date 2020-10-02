from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from screen_helper import screen_helper


class MenuScreen(Screen):
    pass


class ProfileScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))


class DemoApp(MDApp):
    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen


DemoApp().run()
