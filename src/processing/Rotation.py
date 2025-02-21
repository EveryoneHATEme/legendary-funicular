from enum import Enum
from typing import Self, Callable

import numpy as np

from src.data.VertexData import VertexData
from src.processing.Transform import Transform


class Rotation(Transform):
    class Axis(Enum):
        X = 'x'
        Y = 'y'
        Z = 'z'

    def __init__(self,  
                 axis: Axis, 
                 angle: float | None = None,
                 place_horizontally: bool = False,
                 mode: Transform.Mode = Transform.Mode.BOTH) -> None:
        super().__init__(mode)
        self.axis = axis
        self.angle = angle
        self.place_horizontally = place_horizontally

    @classmethod
    def over_another(cls, axis=Axis.Y) -> Self:
        return cls(axis, mode=cls.Mode.RELATIVE)
    
    @classmethod
    def make_horizontal(cls) -> Self:
        return cls(cls.Axis.Y, place_horizontally=True)

    def __call__(self, first_points: VertexData, second_points: VertexData) -> None:
        rotation_source: Callable[[float], np.ndarray]
        match self.axis:
            case self.Axis.X:
                rotation_source = self.get_x_matrix
            case self.Axis.Y:
                rotation_source = self.get_y_matrix
            case self.Axis.Z:
                rotation_source = self.get_z_matrix

        if self.place_horizontally:
            self.angle = self.get_angle_with_x_positive(first_points, second_points)

        match self.mode:
            case self.Mode.BOTH:
                if self.angle is None:
                    raise ValueError("Cannot perform rotation since angle is None")
                rotation_matrix = rotation_source(self.angle)
                first_points.vertex_array @= rotation_matrix
                second_points.vertex_array @= rotation_matrix
            case self.Mode.RELATIVE:
                angle = self.get_angle_between_points(first_points, second_points)
                first_points.vertex_array @= rotation_source(angle)
    
    @staticmethod
    def get_angle_between_points(rotated_points: VertexData, reference_points: VertexData) -> float:
        reference_direction = reference_points[-1] - reference_points[-2]
        rotated_direction = rotated_points[1] - rotated_points[0]

        dot_product = np.dot(reference_direction, rotated_direction)
        norm_product = np.linalg.norm(reference_direction) * np.linalg.norm(rotated_direction)

        return np.arccos(dot_product / norm_product)
    
    @staticmethod
    def get_angle_with_x_positive(first_points: VertexData, second_points: VertexData) -> float:
        current_direction = second_points[1] - first_points[-2]
        desired_direction = np.array([1., 0., 0.])

        dot_product = np.dot(current_direction, desired_direction)
        norm_product = np.linalg.norm(current_direction) * np.linalg.norm(desired_direction)

        return np.arccos(dot_product / norm_product)

    @staticmethod
    def get_x_matrix(angle: float) -> np.ndarray:
        return np.array(
            [[1, 0, 0],
             [0, np.cos(angle), -np.sin(angle)],
             [0, np.sin(angle), np.cos(angle)]]
        )
    
    @staticmethod
    def get_y_matrix(angle: float) -> np.ndarray:
        return np.array(
            [[np.cos(angle), 0, np.sin(angle)],
             [0, 1, 0],
             [-np.sin(angle), 0, np.cos(angle)]]
        )
    
    @staticmethod
    def get_z_matrix(angle: float) -> np.ndarray:
        return np.array(
            [[np.cos(angle), -np.sin(angle), 0],
             [np.sin(angle), np.cos(angle), 0],
             [0, 0, 1]]
        )
