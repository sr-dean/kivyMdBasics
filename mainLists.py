from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import MDList, TwoLineAvatarIconListItem
from kivymd.uix.list import ImageLeftWidget, IconRightWidget
from kivy.uix.scrollview import ScrollView


class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        scroll = ScrollView()
        my_list = MDList()

        for i in range(30):
            img = ImageLeftWidget(source='gerFlag.png')
            icon = IconRightWidget(icon='android')
            item = TwoLineAvatarIconListItem(text='Item ' + str(i),
                                             secondary_text='Hello world')
            item.add_widget(icon)
            item.add_widget(img)
            my_list.add_widget(item)
        scroll.add_widget(my_list)
        screen.add_widget(scroll)
        return screen


DemoApp().run()
