import matplotlib.pyplot as plt

from src.data.VertexData import VertexData
from src.visualization.Plotter import Plotter


class MatplotlibPlotter(Plotter):
    def plot_vertices(self, first_vertices: VertexData, second_vertices: VertexData) -> None:
        figure, axes = plt.subplots()
        axes.plot(first_vertices.vertex_array[:, 0], first_vertices.vertex_array[:, 2], color='g')
        axes.plot(second_vertices.vertex_array[:, 0], second_vertices.vertex_array[:, 2], color='b')
        plt.show()
