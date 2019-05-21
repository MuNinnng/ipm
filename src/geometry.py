# -*- coding: utf-8 -*-
import numpy as np

origin = np.array([
    [0,0,0,1],
    ])
x_axis = np.array([
    [0,0,0,1],
    [1,0,0,1],
    ])
y_axis = np.array([
    [0,0,0,1],
    [0,1,0,1],
    ])
z_axis = np.array([
    [0,0,0,1],
    [0,0,1,1],
    ])

axis = [
    {"geom": x_axis, "type": "line", "color":(0,0,255), "width":2},
    {"geom": y_axis, "type": "line", "color":(0,255,0), "width":2},
    {"geom": z_axis, "type": "line", "color":(255,0,0), "width":2},
]



square = np.array([
    [0,0],
    [0,1],
    [1,1],
    [1,0],
    ])

square = np.array([
    [-3,-1,1,1],
    [-1,1,1,1],
    [1,1,1,1],
    [1,-1,1,1],
    [-1,-1,0,1],
    [-1,1,0,1],
    [1,1,0,1],
    [1,-1,0,1],
    ])

pixels = np.array([
    [500,500]
    ])