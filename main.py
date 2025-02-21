from pathlib import Path

from src.data.VertexData import VertexData
from src.processing import Rdp, Rotation, Transform, Translation
from src.visualization import MatplotlibPlotter, Open3dPlotter

vertex_data_1 = VertexData.from_file(Path('resources') / 'paralepiped_profile_1.ply')
vertex_data_2 = VertexData.from_file(Path('resources') / 'paralepiped_profile_2.ply')

plotter = Open3dPlotter()
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
