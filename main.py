from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from rdp import rdp

from src.data.VertexData import VertexData
from src.processing import Rdp, Rotation, Transform, Translation
from src.visualization.MatplotlibPlotter import MatplotlibPlotter

vertex_data_1 = VertexData.from_file(Path('resources') / 'paralepiped_profile_1.ply')
vertex_data_2 = VertexData.from_file(Path('resources') / 'paralepiped_profile_2.ply')

plotter = MatplotlibPlotter()
plotter.plot_vertices(vertex_data_1, vertex_data_2)

transforms = [
    Rdp(),
    Rotation.over_another(),
    Translation.concatenate(),
    Rotation.make_horizontal(),
    Translation.origin_to_zero()
]

Transform.apply_transforms(vertex_data_2, vertex_data_1, transforms)

plotter.plot_vertices(vertex_data_1, vertex_data_2)
