# -*- coding: utf-8 -*-
import math

import numpy as np


def to_3d(coord):
    w = coord[:,3]
    res = np.zeros(coord.shape)
    print(w)
    res[:,0] = coord[:,0]/w
    res[:,1] = coord[:,1]/w
    res[:,2] = coord[:,2]/w
    return res[:,:3]

class Matrix(object):
    def __init__(self):
        pass

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


if __name__ == "__main__":
    from matplotlib import pyplot as plt

    m = Matrix()
    p_mat = m.perspective(45, 1, 20, 5000)

    p = np.array([[0,0,20, 1]])
    p_new = p @ p_mat
    p_new = np.floor(p_new)
    print(p_new)
    pp = to_3d(p_new)
    print(pp)




    square = np.array([
    [-1,-1,1,1],
    [-1,1,1,1],
    [1,1,1,1],
    [1,-1,1,1],
    [-1,-1,1,1],
    ])

    p_square = square @ p_mat
    p_square3d = to_3d(p_square)
    print(p_square)
    print(square[:,0])
    print(p_square[:,0])

    # plt.scatter(square[:,0], square[:,1])
    plt.scatter(p_square3d[:,0], p_square3d[:,1])
    plt.show()