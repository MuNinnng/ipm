import math

import numpy as np
from matplotlib import pyplot as plt

def translate2d(p, a=0, b=0):
    """Translates point by a and b.

    Returns [x+a, y+b, 1]
    """
    translation_mat = np.matrix([
        [1,0,0],
        [0,1,0],
        [a,b,1]
        ], dtype="float32")

    new_p = p @ translation_mat

    return new_p

def scale2d(p, a=1, b=1):
    """Scales point by a and b.

    Returns [x*a, y*b, 1]

    Note, translation move objects! It scales each axis by some value.
    if you want use scaling by object origin you need to combine it with translation.
    1. move object origin to the space origin
    2. scale object
    3. move object from space origin to its origin
    """
    translation_mat = np.matrix([
        [a,0,0],
        [0,b,0],
        [0,0,1]
        ], dtype="float32")

    new_p = p @ translation_mat

    return new_p

def rotate2d(p, a=0):
    """Rotate point by a."""
    # turn value to radians
    a = math.radians(a)
    translation_mat = np.matrix([
        [math.cos(a),math.sin(a),0],
        [-math.sin(a),math.cos(a),0],
        [0,0,1]
        ], dtype="float32")

    new_p = p @ translation_mat

    return new_p

def show2d(data):
    plt.plot(data[:,0], data[:,1], c="red", marker="o")


if __name__ == "__main__":
    # 2d origin
    origin2d = np.array([
        [0, 0, 1],
        ], dtype="float32")
    square = np.array([
        [-1,-1,1],
        [-1,1,1],
        [1,1,1],
        [1,-1,1],
        [-1,-1,1],
        ])
    # 3d objects in real world

    # cube = np.array([

        # ])

    new_p = rotate2d(square, a=45)
    # new_p = scale2d(new_p, a=2, b=2)
    print(new_p)
    show2d(square)
    show2d(new_p)
    show2d(origin2d)

    plt.show()


    # print(origin)