from abc import ABCMeta, abstractmethod

from src.data.VertexData import VertexData


class Plotter(metaclass=ABCMeta):
    @abstractmethod
    def plot_vertices(self, first_vertices: VertexData, second_vertices: VertexData) -> None:
        ...
