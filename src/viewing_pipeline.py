# -*- coding: utf-8 -*-
from matrix import Transform


class Pipeline(object):
    def __init__(self):
        transform = Transform()

    def camera_transformation(self, points):
        cam_matrix = self.transform.get_camera_matrix()
        return points @ cam_matrix

    def to_image_space(self, points):
        new_points = points @ self.transform.perspective_matrix
        new_points = self.transform.homogenus_to_world(new_points)
        return new_points

    def project(self, points):
        # convert objects to camera view
        res = camera_transform(points)
        # # convert to perspective view
        res = to_image_space(res)
        # # convert to screen view(projection)
        # res = to_screen_space(res)