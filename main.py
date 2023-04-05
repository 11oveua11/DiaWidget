from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.size = (600 , 1000)

class MainApp(App):
    def build(self):
        return Plotter()

class Plotter(BoxLayout):
    pass


MainApp().run()
