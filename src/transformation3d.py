# -*- coding: utf-8 -*-
import math

import numpy as np
from matplotlib import pyplot as plt

def translate2d(p, a=0, b=0, c=0):
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
