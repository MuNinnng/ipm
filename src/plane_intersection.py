# -*- coding: utf-8 -*-
import numpy as np

# dot product is length of vector to vector projection times vector length

# https://www.youtube.com/watch?v=_P829ncXFZY


def ray_plane_intersection(ray_start: np.ndarray, ray_end: np.ndarray,plane_point: np.array, plane_norm: np.array) -> np.ndarray:
    """Calculate plane intersection with ray casted from screen.

    Parameters
    ----------
    ray_start: np.ndarray
        2D array where 1 dim contains amount of rays and 2 dim is ray coordinates
    ray_end: np.ndarray
        2D array where 1 dim contains amount of rays and 2 dim is ray coordinates
    plane_point: np.array
        1D array, vector of any point that is on the plane
    plane_norm: np.array
        1D array of plane normal vector

    Returns
    -------
    np.ndarray
        2D array of intersections points

    Notes
    -----
    All augments should np.ndarray not np.matrix
    """

    # check type
    assert type(ray_start) == np.ndarray, "ray_start has to be numpy array"
    assert type(ray_end) == np.ndarray, "ray_end has to be numpy array"
    assert type(plane_point) == np.ndarray, "plane_point has to be numpy array"
    assert type(plane_norm) == np.ndarray, "plane_norm has to be numpy array"
    # check dims
    assert ray_start.ndim == 2, "ray_start has to be 2 dimensional"
    assert ray_end.ndim == 2, "ray_end has to be 2 dimensional"
    assert plane_point.ndim == 1, "plane_point has to be 1 dimensional"
    assert plane_norm.ndim == 1, "plane_norm has to be 1 dimensional"
    # check shape
    assert ray_start.shape[1] == 3, "ray_start has to have 3 elements in 2 dimensional"
    assert ray_end.shape[1] == 3, "ray_end has to have 3 elements in 2 dimensional"
    assert plane_point.shape[0] == 3, "plane_point has to have 3 elements"
    assert plane_norm.shape[0] == 3, "plane_norm has to have 3 elements"

    # distance from beginning of the ray to its end
    ray_delta = ray_end - ray_start

    # distance from beginning of the ray to the point on the plane
    ray_to_plane_delta = plane_point - ray_start

    # because we use unit vector for plane normal, dot product returns projection
    # of the vector to the norm vector
    ray_proj = np.dot(ray_delta, plane_norm)
    ray_to_plane_proj = np.dot(ray_to_plane_delta, plane_norm)

    # projections gives us scalars which could be treated as perpendicular from ray_start to
    # plane (ray_to_plane_proj) and from ray_start to ray_end(ray_proj).
    # Ration of these two distances are the same as parts of ray which is spitted by plane
    intersection_ratio = ray_to_plane_proj / ray_proj

    # now we could scale ray_delta in according to ration above
    int_ray_delta = (ray_delta.T * intersection_ratio).T

    # add this vector to ray start we will get plane intersection point
    plane_intersection = ray_start + int_ray_delta

    return plane_intersection


if __name__ == "__main__":

    zy_plane_norm = np.array([1,0,0])
    zx_plane_norm = np.array([0,1,0])
    xy_plane_norm = np.array([0,0,1])
    plane_point = np.array([0,0,0])

    r1 = np.array([
        # [10,10,0],
        [10,10,0],
        ])
    r2 = np.array([
        # [-10,10,0],
        [-10,0,0],
        ])

    # r1 = np.array([[0., 0.,5.50100001]])
    # r2 = np.array([[0.,0.,754.49277259]])

    inter = ray_plane_intersection(r1, r2, plane_point, zy_plane_norm)
    print("inter", inter)
    print("inter", type(inter))