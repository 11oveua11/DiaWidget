from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class MainApp(App):
    def build(self):
        return Plotter()

class Plotter(BoxLayout):
    pass


MainApp().run()
