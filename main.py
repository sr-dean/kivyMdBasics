from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (300,500)

navigation_helper = """
Screen:
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Demo App'
                        left_action_items: [["menu",lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 11
                    Widget:
        MDNavigationDrawer: 
            id: nav_drawer         

"""


class DemoApp(MDApp):
    def build(self):
        screen = Builder.load_string(navigation_helper)
        return screen

DemoApp().run()