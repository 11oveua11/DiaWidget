from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy_garden.graph import Graph
import numpy as np

Window.size = (400 , 800)

class MainApp(App):
    def build(self):
        return Plotter()

class Plotter(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.graph = Graph()
        self.ids.graph.add_widget(self.graph)


MainApp().run()
