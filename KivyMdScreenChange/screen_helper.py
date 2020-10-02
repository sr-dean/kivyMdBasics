screen_helper = """
ScreenManager:
    MenuScreen:
    ProfileScreen:

<MenuScreen>:
    name:'menu'
    MDRectangleFlatButton:
        text:'Profile'
        pos_hint:{'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current = 'profile'

<ProfileScreen>:
    name:'profile'
    MDLabel:
        text:'Welcome to the profile page'
        halign: 'center'
    MDRectangleFlatButton:
        text:'Menu'
        pos_hint:{'center_x':0.5,'center_y':0.4}
        on_press: root.manager.current = 'menu'

"""
