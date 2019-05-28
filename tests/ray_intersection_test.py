# -*- coding: utf-8 -*-

import numpy as np

from src.plane_intersection import ray_plane_intersection


def test_ray_to_plane_intersection():
    zx_plane_norm = np.array([0,1,0])
    zy_plane_norm = np.array([1,0,0])
    xy_plane_norm = np.array([0,0,1])
    plane_point = np.array([0,0,0])

    ray_start = np.array([
        [10,10,0],
        [10,10,0],
        [10,10,0],
        ])

    ray_end = np.array([
        [-10,10,0],
        [-10,0,0],
        [-10,-10,0],
        ])

    expected = np.array([
        [0.,10.,0.],
        [0.,5.,0.],
        [0.,0.,0.],
        ])

    intersected = ray_plane_intersection(ray_start, ray_end, plane_point, zy_plane_norm)

    assert np.all(intersected == expected), "Intersections are not correct!"
