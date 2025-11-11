from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty


class ConvertMilesToKmApp(App):
    """ConvertMilesToKmApp is a Kivy app for converting miles to km"""
    message = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (500, 400)
        self.title = "Convert miles to km"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self):
        number = float(self.root.ids.input_field.text)
        output = number * 1.60934
        self.message = output


ConvertMilesToKmApp().run()
