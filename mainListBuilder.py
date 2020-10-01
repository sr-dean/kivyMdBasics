from kivymd.app import MDApp
# Other imports will be made automatically by the builder method
from kivy.lang import Builder
from kivymd.uix.list import TwoLineAvatarListItem, ImageLeftWidget


list_helper = """
Screen:
    ScrollView:
        MDList:
            id: container

"""


class DemoApp(MDApp):
    def build(self):
        screen = Builder.load_string(list_helper)

        return screen

    def on_start(self):  # on_start and build methods are automatically called
        for i in range(20):
            item = TwoLineAvatarListItem(text='item ' + str(i), secondary_text='Hello World')
            img = ImageLeftWidget(source='itaFlag.png')
            item.add_widget(img)
            self.root.ids.container.add_widget(item)


DemoApp().run()
