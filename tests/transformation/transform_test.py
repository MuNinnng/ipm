# -*- coding: utf-8 -*-
from src.transform import transform


def test_x_translation():
    t = Transform()

    p = np.array([
        [0, 0, 0, 1],
        ], dtype="float32")

    expect_p = np.array([
        [1, 0, 0, 1],
        ], dtype="float32")

    new_p = t.set_translation(x=1)

    assert np.all(new_p == expect_p), "Translation for X axis does not correct"


def test_y_translation():
    t = Transform()

    p = np.array([
        [0, 0, 0, 1],
        ], dtype="float32")

    expect_p = np.array([
        [0, 1, 0, 1],
        ], dtype="float32")

    new_p = t.set_translation(y=1)

    assert np.all(new_p == expect_p), "Translation for Y axis does not correct"


def test_z_translation():
    t = Transform()

    p = np.array([
        [0, 0, 0, 1],
        ], dtype="float32")

    expect_p = np.array([
        [0, 0, 1, 1],
        ], dtype="float32")

    new_p = t.set_translation(z=1)

    assert np.all(new_p == expect_p), "Translation for Z axis does not correct"


def test_all_translation():
    t = Transform()

    p = np.array([
        [0, 0, 0, 1],
        ], dtype="float32")

    expect_p = np.array([
        [100, 12, -2, 1],
        ], dtype="float32")

    new_p = t.set_translation(x=100,y=12,z=-2)

    assert np.all(new_p == expect_p), "Translation for ALL axis does not correct"