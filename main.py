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
        self.samples = 32
        self.graph = Graph(xmin=0, xmax=self.samples, ymin=-1, ymax=1,
                           border_color=[0,1,1,1], tick_color=[0,1,1,0.7],
                           x_grid=True, y_grid=True, draw_border=True,
                           x_grid_label=True, y_grid_label=False,
                           x_ticks_major=4, y_ticks_major=0.4)
        self.ids.graph.add_widget(self.graph)
        self.plot_x = np.linspace(0, 1, self.samples)
        self.plot_y = np.sin(4*np.pi*self.plot_x)
        self.plot = LinePlot(color=[1,1,0,1], line_width=1.5)
        self.plot.points = ([(x, self.plot_y[x]) for x in range(self.samples)])
        self.graph.add_plot(self.plot)

    def update_plot (self):
        pass

MainApp().run()
