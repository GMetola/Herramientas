from open3d import *
import numpy as np

joue = open3d.read_point_cloud("./fragment.pcd")
draw_geometries([joue])

joue.paint_uniform_color([0.7, 0.7, 0.7])
joue_tree = KDTreeFlann(joue)

[k, idx, _] = joue_tree.search_radius_vector_3d(joue.points[1500],0.2)
np.asarray(joue.colors)[idx[1:], :] = [0, 1, 0]
draw_geometries([joue])