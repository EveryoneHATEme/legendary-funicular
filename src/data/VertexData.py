from dataclasses import dataclass
from pathlib import Path
from typing import Self, TypeAlias

import numpy as np
from plyfile import PlyData


IndexType: TypeAlias = int | slice | tuple[int | slice, ...]


@dataclass
class VertexData:
    vertex_array: np.ndarray

    def __getitem__(self, index: IndexType) -> float | np.ndarray:
        return self.vertex_array[index]
    
    def __setitem__(self, index: IndexType, value: float | np.ndarray) -> None:
        self.vertex_array[index] = value

    @classmethod
    def from_file(cls, path: Path) -> Self:
        with open(path, 'rb') as file:
            raw_data = PlyData.read(file)
        
        cls.check_raw_data_format(raw_data)

        vertex_raw_data = raw_data['vertex']
        vertex_array = np.vstack([vertex_raw_data['x'], vertex_raw_data['y'], vertex_raw_data['z']]).T

        return cls(vertex_array)
        
    @staticmethod
    def check_raw_data_format(raw_data: PlyData) -> None:
        if 'vertex' not in raw_data._element_lookup:
            raise WrongFileFormat(f"No element called 'vertex' in the provided file")
        
        if 'x' not in raw_data['vertex']._property_lookup:
            raise WrongFileFormat(f"The file doesn't contain 'x' coordinates")
        if 'y' not in raw_data['vertex']._property_lookup:
            raise WrongFileFormat(f"The file doesn't contain 'y' coordinates")
        if 'z' not in raw_data['vertex']._property_lookup:
            raise WrongFileFormat(f"The file doesn't contain 'z' coordinates")


class WrongFileFormat(Exception):
    pass