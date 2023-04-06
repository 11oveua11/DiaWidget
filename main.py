from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy_garden.graph import Graph, LinePlot
import numpy as np

Window.size = (400 , 800)

class MainApp(App):
    def build(self):
        return Plotter()

class Plotter(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.samples = 512
        self.graph = Graph(xmin=0, xmax=512, ymin=0, ymax=512)
        self.ids.graph.add_widget(self.graph)
        self.plot_x = np.linspace(0,1, self.samples)
        self.plot_y = np.linspace(0,1, self.samples)
        self.plot = LinePlot()
        self.plot.points = [range(2)]

MainApp().run()
