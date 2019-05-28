# -*- coding: utf-8 -*-
import numpy as np

from transform import Transform

from renderer import Viewport


class Pipeline(object):
    def __init__(self, viewport, proj_matrix=None):
        self.transform = Transform()
        self.viewport = Viewport(viewport)
        self.proj_matrix = proj_matrix

    def calc_proj_matrix(self):
        camera_mat = self.transform.get_camera_matrix()
        perspective_mat = self.transform.perspective_matrix

        project_mat = camera_mat @ perspective_mat

        return project_mat

    def get_proj_matrix(self):
        if self.proj_matrix is not None:
            return self. proj_matrix
        else:
            return self.calc_proj_matrix()

    def project(self, points):
        points = self.transform.world_to_homogenus(points)

        project_mat = self.get_proj_matrix()

        res = points @ project_mat
        res = self.transform.homogenus_to_world(res)
        return res

    def unproject(self, pixels):
        # the Normalized Device Coordinates (NDC).
        # turn pixel value to Image space coordinates
        ndc_near_coords = self.viewport.pixel_to_ndc_coord(pixels)
        ndc_far_coords = np.copy(ndc_near_coords)
        # set pixel point at far plane
        ndc_far_coords[:, 2] = 1

        unproject_mat = np.linalg.inv(self.get_proj_matrix())

        new_near_points = ndc_near_coords @ unproject_mat
        new_near_points = self.transform.homogenus_to_world(new_near_points)

        new_far_points = ndc_far_coords @ unproject_mat
        new_far_points = self.transform.homogenus_to_world(new_far_points)

        vec = new_far_points - new_near_points
        return new_near_points, new_far_points

    def draw(self, objects):
        for obj in objects:
            if obj["type"] == "line":
                projected = self.project(obj["geom"])
                self.viewport.draw_lines(projected, color=obj["color"], width=obj["width"])
            if obj["type"] == "point":
                projected = self.project(obj["geom"])
                self.viewport.draw_points(projected, color=obj["color"], size=obj["size"])

    def show(self):
        plt.imshow(self.viewport.image)
        # inverse Y axis because of image coord system
        plt.show()


if __name__ == "__main__":
    from matplotlib import pyplot as plt
    import geometry as g
    from plane_intersection import ray_plane_intersection


    pl = Pipeline(viewport=(500,500))
    # pl.transform.set_camera([0, 0, -10])
    pl.transform.set_translation(y=0,x=0,z=-5)
    pl.transform.rotate_x(20)
    pl.transform.rotate_y(20)

    screen_point = np.array([
        [0,0],
        [500,500],
        [250,250],
        # [350,250],
        # [250,350],
        # [450,450],
        # [10,10],
        # [260,270],
        # [250,0],
        # [250,300],
        ])

    n_points, f_points = pl.unproject(screen_point)
    zy_plane_norm = np.array([1,0,0])
    zx_plane_norm = np.array([0,1,0])
    xy_plane_norm = np.array([0,0,1])
    plane_point = np.array([0,0,0])

    test = [
        {"geom": f_points, "type": "point", "color":(0,255,255), "size":6},
        {"geom": n_points, "type": "point", "color":(255,0,0), "size":4},
    ]

    # calc intersection
    # inter = ray_plane_intersection(n_points, f_points, plane_point, xy_plane_norm)
    inter = ray_plane_intersection(n_points, f_points, plane_point, zx_plane_norm)
    i = [
        {"geom": inter, "type": "point", "color":(255,255,0), "size":2},
    ]
    # pl.viewport.draw_points(inter, color=(255,255,0), size=3)
    pl.draw(g.axis)
    pl.draw(test)
    # pl.transform.rotate_y(90)
    pl.draw(i)
    pl.show()
   
