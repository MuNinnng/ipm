import numpy as np
from matplotlib import pyplot as plt

import geometry as g
from plane_intersection import ray_plane_intersection
from viewing_pipeline import Pipeline


# Camera 1
cam1 = Pipeline(viewport=(100,100))
cam1.transform.set_translation(y=0,x=0,z=-5)

cam1_screen_point = np.array([
    [25,25],
    [25,75],

    [75,25],
    [75,75],
    ])

cam1_n_points, cam1_f_points = cam1.unproject(cam1_screen_point)
zy_plane_norm = np.array([1,0,0])
zx_plane_norm = np.array([0,1,0])
xy_plane_norm = np.array([0,0,1])
plane_point = np.array([0,0,0])

cam1_vec = cam1_f_points - cam1_n_points

# print(cam1_vec)

# Camera 2
cam2 = Pipeline(viewport=(100,100))
cam2.transform.set_translation(y=0,x=0,z=-5)
cam2.transform.rotate_x(20)
cam2.transform.rotate_y(180)

cam2_screen_point = np.array([
    [25,25],
    [25,75],

    [75,25],
    [75,75],
    ])

cam2_n_points, cam2_f_points = cam2.unproject(cam1_screen_point)
zy_plane_norm = np.array([1,0,0])
zx_plane_norm = np.array([0,1,0])
xy_plane_norm = np.array([0,0,1])
plane_point = np.array([0,0,0])

cam2_vec = cam2_f_points - cam2_n_points

# get planes norms
# print(cam2_vec)
cam2_lb_norm = np.cross(cam2_vec[0], cam2_vec[1])
cam2_rb_norm = np.cross(cam2_vec[2], cam2_vec[3])

cam1_inter1 = ray_plane_intersection(cam1_n_points, cam1_f_points, cam2_n_points[0], cam2_lb_norm)
cam1_inter2 = ray_plane_intersection(cam1_n_points, cam1_f_points, cam2_n_points[2], cam2_rb_norm)


print(cam1_inter1)
print(cam1_inter2)

# test = [
#     {"geom": f_points, "type": "point", "color":(0,255,255), "size":6},
#     {"geom": n_points, "type": "point", "color":(255,0,0), "size":4},
# ]

# # calc intersection
# # inter = ray_plane_intersection(n_points, f_points, plane_point, xy_plane_norm)
# i = [
#     {"geom": inter, "type": "point", "color":(255,255,0), "size":2},
# ]
# # pl.viewport.draw_points(inter, color=(255,255,0), size=3)
# pl.draw(g.axis)
# pl.draw(test)
# # pl.transform.rotate_y(90)
# pl.draw(i)
# pl.show()
#    