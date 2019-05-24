# -*- coding: utf-8 -*-
import numpy as np

from plane_intersection import ray_plane_intersection
from viewing_pipeline import Pipeline
from utils import get_pixel_coords


def ipm(image_size, vangle=45):
    """Calculate map of image pixel to invert image projection."""

    pl = Pipeline(viewport=image_size)
    pl.transform.rotate_x(vangle)

    # prepare matrix of scree pixels coordinates
    screen_pixels = get_pixel_coords(image_size)

    # convert screen pixel to ray in NDS
    n_points, f_points = pl.unproject(screen_pixels)

    # ZX plane normal
    zx_plane_norm = np.array([0,1,0])
    plane_point = np.array([0,0,0])

    inv_projected_pixels = ray_plane_intersection(
        n_points, f_points, plane_point, zx_plane_norm)

    # Use Z value as Y value
    ipm_coord = np.zeros((inv_projected_pixels.shape[0], 2))
    ipm_coord[:,0] = inv_projected_pixels[:,0]
    ipm_coord[:,1] = inv_projected_pixels[:,2]

    # convert everything to 1 quarter
    xmin = np.min(ipm_coord[:,0])
    ymin = np.min(ipm_coord[:,1])

    ipm_coord[:,0] = ipm_coord[:,0] + (xmin*-1)
    ipm_coord[:,1] = ipm_coord[:,1] + (ymin*-1)

    # change Y axis origin
    # ymax = np.max(ipm_coord[:,1])
    # ipm_coord[:,1] = ymax - ipm_coord[:,1]

    # normalize over biggest value
    ipm_coord_norm = ipm_coord / np.max(ipm_coord)



    return screen_pixels, ipm_coord_norm