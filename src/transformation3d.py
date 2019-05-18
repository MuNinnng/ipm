# -*- coding: utf-8 -*-
import math

import numpy as np
from matplotlib import pyplot as plt

def translate3d(p, a=0, b=0, c=0):
    """Translates point by a, b and c.

    Returns [x+a, y+b, z+c, 1]
    """
    translation_mat = np.matrix([
        [1,0,0,0],
        [0,1,0,0],
        [0,0,1,0],
        [a,b,c,1]
        ], dtype="float32")

    new_p = p @ translation_mat

    return new_p

def scale3d(p, a=1, b=1, c=1):
    """Scales point by a, b and c.

    Returns [x*a, y*b, z*c, 1]

    Note, translation move objects! It scales each axis by some value.
    if you want use scaling by object origin you need to combine it with translation.
    1. move object origin to the space origin
    2. scale object
    3. move object from space origin to its origin
    """
    translation_mat = np.matrix([
        [a,0,0,0],
        [0,b,0,0],
        [0,0,c,0],
        [0,0,0,1],
        ], dtype="float32")

    new_p = p @ translation_mat

    return new_p
