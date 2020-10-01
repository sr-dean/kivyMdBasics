from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window  # for testing only

Window.size = (300, 500)  # for testing only, remove from final version
screen_helper = """
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Demo App'
            md_bg_color: app.theme_cls.primary_dark
            left_action_items: [["menu",lambda x: app.navigation_draw()]]
            right_action_items: [["clock",lambda x: app.navigation_draw()]]
            elevation: 11 #creates a shadow, giving impression that toolbar is elevated
        MDLabel:
            size_hint:(0.5,0.5)
            text: 'Hello World'
            halign: 'center'
        MDBottomAppBar:
            MDToolbar:
                title: 'Help'
                left_action_items: [["coffee",lambda x: app.navigation_draw()]]
                mode: 'end' # changes the position of the action button
                type: 'bottom' # changes appearance of action button
                icon: 'rowing'
                on_action_button: app.navigation_draw() # lambda not needed as it is a built in function of action button
"""


class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Green'
        screen = Builder.load_string(screen_helper)
        return screen

    def navigation_draw(self):
        print("Navigation")


DemoApp().run()
