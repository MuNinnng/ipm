# -*- coding: utf-8 -*-
import numpy as np

from src.transform import Transform


def test_x_translation():
    t = Transform()

    p = np.array([
        [0, 0, 0, 1],
        ], dtype="float64")

    expect_p = np.array([
        [1, 0, 0, 1],
        ], dtype="float64")

    t.set_translation(x=1)
    new_p = p @ t.view_matrix

    assert np.all(new_p == expect_p), "Translation for X axis does not correct"


def test_y_translation():
    t = Transform()

    p = np.array([
        [0, 0, 0, 1],
        ], dtype="float64")

    expect_p = np.array([
        [0, 1, 0, 1],
        ], dtype="float64")

    t.set_translation(y=1)
    new_p = p @ t.view_matrix

    assert np.all(new_p == expect_p), "Translation for Y axis does not correct"


def test_z_translation():
    t = Transform()

    p = np.array([
        [0, 0, 0, 1],
        ], dtype="float64")

    expect_p = np.array([
        [0, 0, 1, 1],
        ], dtype="float64")

    t.set_translation(z=1)
    new_p = p @ t.view_matrix

    assert np.all(new_p == expect_p), "Translation for Z axis does not correct"


def test_all_translation():
    t = Transform()

    p = np.array([
        [0, 0, 0, 1],
        ], dtype="float64")

    expect_p = np.array([
        [100, 12, -2, 1],
        ], dtype="float64")

    t.set_translation(x=100,y=12,z=-2)
    new_p = p @ t.view_matrix

    assert np.all(new_p == expect_p), "Translation for ALL axis does not correct"