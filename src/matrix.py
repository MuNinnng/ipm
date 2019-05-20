# -*- coding: utf-8 -*-

class Matrix(object):

    def perspective(self, fov, aspect, near, far):
        """Generates a perspective projection matrix with given bounds.

        :param fov: vertical field of view
        :param aspect: aspect ratio - typically viewport width/height
        :param near: - near bounds of the frustum
        :param far: - far bounds of the frustum

        :return: new 4x4 np.matrix
        """

        pass