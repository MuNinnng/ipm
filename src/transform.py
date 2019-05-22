# -*- coding: utf-8 -*-
import math

import numpy as np


class Transform(object):
    def __init__(self):
        self.view_matrix = np.identity(4)
        # FIXME: use arguments during initialization of the class
        self.perspective_matrix = self.perspective(45,1,1,500)

    def set_translation(self, x=0, y=0, z=0):
        """Translates point by a, b and c.

        Returns [x+a, y+b, z+c, 1]
        """
        translation_mat = np.array([
            [1,0,0,0],
            [0,1,0,0],
            [0,0,1,0],
            [x,y,z,1]
            ], dtype="float64")

        self.view_matrix = self.view_matrix @ translation_mat

    def rotate_y(self, a=0):
        """Rotate point by a."""
        # turn value to radians
        a = math.radians(a)
        translation_mat = np.array([
            [math.cos(a),0,-math.sin(a),0],
            [0,1,0,0],
            [math.sin(a),0,math.cos(a),0],
            [0,0,0,1],
            ], dtype="float32")

        self.view_matrix = self.view_matrix @ translation_mat

    def rotate_z(self, a=0):
        """Rotate point by a."""
        # turn value to radians
        a = math.radians(a)
        translation_mat = np.array([
            [math.cos(a),math.sin(a),0,0],
            [-math.sin(a),math.cos(a),0,0],
            [0,0,1,0],
            [0,0,0,1],
            ], dtype="float32")

        self.view_matrix = self.view_matrix @ translation_mat

    def set_camera(self, position):
        """Set camera position in world coordinates.

        Use minus sign, because camera movements are mirrored to the
        world transformation. If we translate Z axis for 1 step back(-1) in world, it means to
        make 1 step forward(+1) for camera.
        """
        self.view_matrix[3,0] = position[0]
        self.view_matrix[3,1] = position[1]
        self.view_matrix[3,2] = position[2]

    def get_camera_matrix(self):
        return np.linalg.inv(self.view_matrix)

    def homogenus_to_world(self, points):
        w = points[:,3]
        res = np.zeros(points.shape)
        res[:,0] = points[:,0]/w
        res[:,1] = points[:,1]/w
        res[:,2] = points[:,2]/w
        return res[:,:3]

    def world_to_homogenus(self, points):
        h = np.ones((points.shape[0],points.shape[1]+1))
        h[:,:-1] = points
        return h

    def perspective(self, fov, aspect, near, far):
        """Generates a perspective projection matrix with given bounds.

        :param fov: vertical field of view
        :param aspect: aspect ratio - typically viewport width/height
        :param near: - near bounds of the frustum
        :param far: - far bounds of the frustum

        :return: new 4x4 np.matrix
        """

        dist = far - near

        a = (far+near)/dist
        # b = (2*near*far)/dist
        b = (2*near*far)/(near - far)

        alpha = math.radians(fov/2)
        # print(alpha)
        # calc contagent
        cot = 1. / math.tan(alpha)

        perspective_mat = np.array([
            [cot,0,0,0],
            [0,cot,0,0],
            [0,0,a,1],
            [0,0,b,1]
            ], dtype="float32")

        return perspective_mat
