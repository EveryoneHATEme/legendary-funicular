from rdp import rdp

from src.data.VertexData import VertexData
from src.processing.Transform import Transform


class Rdp(Transform):
    def __init__(self, epsilon=0.001) -> None:
        super().__init__()
        self.epsilon = epsilon

    def __call__(self, first_points: VertexData, second_points: VertexData) -> None:
        match self.mode:
            case self.Mode.BOTH:
                first_points.vertex_array = rdp(first_points.vertex_array, epsilon=self.epsilon)
                second_points.vertex_array = rdp(second_points.vertex_array, epsilon=self.epsilon)
            case self.Mode.RELATIVE:
                raise NotImplementedError("RDP in relative mode is undefined")
