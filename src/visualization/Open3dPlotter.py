import open3d
import open3d.visualization

from src.data.VertexData import VertexData
from src.visualization.Plotter import Plotter


class Open3dPlotter(Plotter):
    def plot_vertices(self, first_vertices: VertexData, second_vertices: VertexData) -> None:
        first_vectors = open3d.utility.Vector3dVector(first_vertices.vertex_array)
        first_point_cloud = open3d.geometry.PointCloud(first_vectors)
        first_point_cloud.paint_uniform_color((0., 1., 0.))

        first_lines = [(i, i + 1) for i in range(len(first_vertices.vertex_array) - 1)]
        first_line_set = open3d.geometry.LineSet(
            points=first_vectors,
            lines=open3d.utility.Vector2iVector(first_lines)
        )
        first_line_set.paint_uniform_color((0., 0.8, 0.))

        second_vectors = open3d.utility.Vector3dVector(second_vertices.vertex_array)
        second_point_cloud = open3d.geometry.PointCloud(second_vectors)
        second_point_cloud.paint_uniform_color((0., 0., 1.))

        second_lines = [(i, i + 1) for i in range(len(second_vertices.vertex_array) - 1)]
        second_line_set = open3d.geometry.LineSet(
            points=second_vectors,
            lines=open3d.utility.Vector2iVector(second_lines)
        )
        second_line_set.paint_uniform_color((0., 0., 0.8))

        open3d.visualization.draw_geometries(
            [first_point_cloud,
             first_line_set, 
             second_point_cloud, 
             second_line_set]
        )
