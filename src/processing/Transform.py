from abc import ABCMeta, abstractmethod
from enum import Enum
from functools import reduce
from typing import Self

from src.data.VertexData import VertexData


class Transform(metaclass=ABCMeta):
    class Mode(Enum):
        BOTH = 'both'
        RELATIVE = 'relative'

    @abstractmethod
    def __init__(self, mode: Mode = Mode.BOTH) -> None:
        self.mode = mode

    @abstractmethod
    def __call__(self, first_points: VertexData, second_points: VertexData) -> None:
        ...
    
    @staticmethod
    def apply_transforms(first_points: VertexData, second_points: VertexData, transforms: list[Self]):
        for transform in transforms:
            transform(first_points, second_points)
