from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class ConvertMilesToKmApp(App):
    """ConvertMilesToKmApp is a Kivy app for converting miles to km"""
    km = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (500, 400)
        self.title = "Convert miles to km"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, text):
        """Handle calculation (could be button press or other call)."""
        miles = self.convert_to_number(text)
        self.update_result(miles)

    def handle_increment(self, text, change):
        """Handle up/down button press, update the text input with new value, call calculation function."""
        miles = self.convert_to_number(text) + change
        self.root.ids.input_miles.text = str(miles)

    def update_result(self, miles):
        self.km = str(miles * MILES_TO_KM)

    @staticmethod
    def convert_to_number(text):
        """Convert text to float or 0.0 if invalid."""
        try:
            return float(text)
        except ValueError:
            return 0.0


ConvertMilesToKmApp().run()
