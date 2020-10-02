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
            BoxLayout:
                orientation:'vertical'
                spacing: '8dp'#dp=display pixels
                padding: '8dp'
                Image:
                    source: 'mePic.jpg'
                MDLabel:
                    text:'Stuart Dean'
                    font_style:'Subtitle1'      
                    size_hint_y:None
                    height:self.texture_size[1]#reduces the size of the label to the size of the text
                MDLabel:
                    text:'sr-dean15@live.co.uk'
                    font_style:'Caption'
                    size_hint_y:None
                    height:self.texture_size[1]
                
                ScrollView:#pushes all widgets to the top 
                    MDList:
                        OneLineIconListItem:
                            text:'Go to race'
                            IconLeftWidget:
                                icon:'rowing'
                        OneLineIconListItem:
                            text:'Select difficulty'
                            IconLeftWidget:
                                icon:'android'

"""


class DemoApp(MDApp):
    def build(self):
        screen = Builder.load_string(navigation_helper)
        return screen

DemoApp().run()