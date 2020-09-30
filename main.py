from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp


class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        table = MDDataTable(pos_hint=
                            {'center_x': 0.5, 'center_y': 0.5},
                            size_hint=(0.9, 0.6),
                            check=True,
                            rows_num=10,#allows scrolling
                            column_data=[("Food", dp(40)),
                                         ("Calories", dp(15)),
                                         ("Taste", dp(10))],
                            row_data=[("Burger", "300", "7"),
                                      ("Pizza", "720", "8"),
                                      ("Pizza", "760", "8"),
                                      ("Pizza", "720", "8"),
                                      ("Pizza", "770", "8"),
                                      ("Pizza", "780", "8"),
                                      ("Pizza", "790", "8"),
                                      ("Pizza", "710", "8"),
                                      ("Pizza", "740", "8"),
                                      ("Pizza", "730", "8")])
        table.bind(on_check_press=self.check_press)
        table.bind(on_row_press=self.row_press)
        screen.add_widget(table)

        return screen

    def check_press(self, instance_table, current_row):
        print(instance_table, current_row)

    def row_press(self, instance_table, current_row):
        print(instance_table, current_row)


DemoApp().run()
