# -*- coding: utf-8 -*-
import numpy as np


def get_pixel_coords(size):
    grid_w, grid_h = size
    grid_h_indices = list(range(grid_h)) * grid_w
    cell_h = np.reshape(grid_h_indices, (grid_w, grid_h))
    cell_w = np.array([[el]*grid_h for el in range(grid_w)])
    cell_h = np.reshape(cell_h, [grid_w, grid_h, 1])
    cell_w = np.reshape(cell_w, [grid_w, grid_h, 1])

    grid = np.concatenate([cell_w, cell_h], axis=-1)
    w, h, p = grid.shape
    pixels = np.reshape(grid, [w*h, p])

    return pixels