from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivy.lang import Builder

 
class Pikka(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        screen = Screen()
        username_input = """
MDTextField:
    hint_text: "Enter username"
    helper_text: "ur dumb haha"
    helper_text_mode: "on_focus"
    icon_right: ""
    icon_right_color: app.theme_cls.primary_color
    pos_hint:{'center_x': 0.5, 'center_y': 0.5}
    size_hint_x:None
    width:300
"""

        self.username = Builder.load_string(username_input)
        button = MDRectangleFlatButton(text='Show',
                                       pos_hint={'center_x': 0.5, 'center_y': 0.3},
                                       on_release=self.show_data)
        screen.add_widget(self.username)
        screen.add_widget(button)
        return screen

    def show_data(self,obj):
        print(self.username.text)

 
 
if __name__ == "__main__":
    Pikka().run()
