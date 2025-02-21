from typing import Self

import numpy as np

from src.data.VertexData import VertexData
from src.processing.Transform import Transform


class Translation(Transform):
    def __init__(self, 
                 translation_vector: np.ndarray | None = None, 
                 to_zero: bool = False,
                 mode: Transform.Mode = Transform.Mode.BOTH) -> None:
        super().__init__(mode)
        self.translation_vector = translation_vector
        self.to_zero = to_zero
    
    @classmethod
    def concatenate(cls) -> Self:
        return cls(mode=cls.Mode.RELATIVE)
    
    @classmethod
    def origin_to_zero(cls) -> Self:
        return cls(to_zero=True)

    def __call__(self, first_points: VertexData, second_points: VertexData) -> None:
        if self.to_zero:
            self.translation_vector = self.get_origin_offset(first_points, second_points)

        match self.mode:
            case self.Mode.BOTH:
                first_points.vertex_array += self.translation_vector
                second_points.vertex_array += self.translation_vector
            case self.Mode.RELATIVE:
                self.translation_vector = second_points[-1] - first_points[0]
                first_points.vertex_array += self.translation_vector
    
    @staticmethod
    def get_origin_offset(first_points: VertexData, second_points: VertexData) -> None:
        return -np.min(np.vstack([first_points.vertex_array, second_points.vertex_array]), axis=0)
