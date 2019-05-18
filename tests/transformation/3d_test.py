# -*- coding: utf-8 -*-
import numpy as np

from src import transformation3d as t


def test_z_rotation():
    p = np.array([
        [1, 0, 0, 1],
        ], dtype="float32")

    expect_p = np.array([
        [0, 1, 0, 1],
        ], dtype="float32")

    new_p = t.rotate_z(p, a=90)
    # new values are not exectly the same, let round it
    new_p = np.floor(new_p)

    assert np.all(new_p == expect_p), "Transformation along Z axis does not correct"


def test_x_rotation():
    p = np.array([
        [0, 1, 0, 1],
        ], dtype="float32")

    expect_p = np.array([
        [0, 0, 1, 1],
        ], dtype="float32")

    new_p = t.rotate_x(p, a=90)
    # new values are not exectly the same, let round it
    new_p = np.floor(new_p)

    assert np.all(new_p == expect_p), "Transformation along X axis does not correct"


def test_y_rotation():
    p = np.array([
        [0, 0, 1, 1],
        ], dtype="float32")

    expect_p = np.array([
        [1, 0, 0, 1],
        ], dtype="float32")

    new_p = t.rotate_y(p, a=90)
    # new values are not exectly the same, let round it
    new_p = np.floor(new_p)

    assert np.all(new_p == expect_p), "Transformation along Y axis does not correct"

