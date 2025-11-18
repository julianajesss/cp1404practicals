from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Kivy app to create labels for every element of NAMES."""

    def __init__(self, **kwargs):
        """Construct the main app."""
        super().__init__(**kwargs)
        self.names = ("name 1", "name 2", "name 3", "name 4")

    def build(self):
        """Build Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from data and add them to the GUI."""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp.run()
