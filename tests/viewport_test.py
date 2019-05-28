# -*- coding: utf-8 -*-

import numpy as np

from src.renderer import Viewport

def test_pixel_dims():
    ndc_points = np.array([
        [-1,-1,0,1],
        [0,0,0,1],
        [.5,.5,0,1],
        [1,1,0,1],
        ])

    vp = Viewport((500,500))
    res = vp.ndc_coord_to_pixel(ndc_points)

    assert res.ndim == 2, "Dims are not correct, it always has to be 2 ndim"


def test_image_index_offset():
    ndc_points = np.array([
        [-1,-1,0,1],
        [0,0,0,1],
        [.5,.5,0,1],
        [1,1,0,1],
        ])

    vp = Viewport((500,500))
    pixel_coord = vp.ndc_coord_to_pixel(ndc_points)
    max_pixel_val = np.max(pixel_coord)

    assert max_pixel_val == 500-1, "Indexing is broken!"


def test_ndc_to_pixel_to_ndc():
    ndc_points = np.array([
        [-1,-1,0,1],
        [0,0,0,1],
        [.5,.5,0,1],
        [1,1,0,1],
        ])

    expectation = ndc_points[:, :2]

    vp = Viewport((500,500))
    res = vp.ndc_coord_to_pixel(ndc_points)
    res = vp.pixel_to_ndc_coord(res)
    # results are not exactly the same due to float operations, round is required
    res = np.round(res, 2)
    res = res[:,:2]

    assert np.all(res == expectation), "Calculations are seems to be wrong, loop does not work"