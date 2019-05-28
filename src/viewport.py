# -*- coding: utf-8 -*-
from typing import Tuple

import numpy as np
from PIL import Image, ImageDraw


class Viewport(object):
    """Draw geometry objects on image.

    Viewport allows to visualize viewing transformation results of 3D scene.
    It represents camera viewing results.

    Attributes
    ----------
    size: tuple of ints
        viewport size in pixels.
    image: PIL Image
        contains viewport drawing results
    d:
        Pillow drawing object

    """

    def __init__(self, size: Tuple[int, int]) -> None:
        self.size = size
        self.image = Image.new('RGB', size, color=(255,255,255))
        self.d = ImageDraw.Draw(self.image)

    def ndc_coord_to_pixel(self, points: np.ndarray) -> np.ndarray:
        """Convert data from image space(NDC) to screen space.

        Converts from NDC to Image Space:

        (-1,1)       (1,1)       (0,0)       (w,0)
            +---------+             +---------+
            |         |             |         |
            |    +    |     -->     |         |
            |  (0,0)  |             |         |
            +---------+             +---------+
        (-1,-1)      (1,-1)      (0,h)       (w,h)

        Parameters
        ---------
        points: np.ndarray
            2D array of points with shape (N of points, 3). Points value should be in range form -1 to 1


        Returns
        -------
        np.ndarray
            2D array of shape (N of points, 2)

        """

        w,h = self.size
        # reduce size because of 0 based indexing, so num 500 has 499 index
        w -= 1
        h -= 1

        pixels = np.copy(points)
        pixels[:,0] = (pixels[:,0] + 1)*w/2
        # Flip Y axis origin
        pixels[:,1] = (1 - pixels[:,1])*h/2
        pixels = pixels[:,:2].astype(int)

        return pixels

    def pixel_to_ndc_coord(self, pixels: np.ndarray) -> np.ndarray:
        """Convert pixel values to Normalized Device Coordinates."""
        w,h = self.size
        # reduce size because of 0 based indexing, so num 500 has 499 index
        w -= 1
        h -= 1

        ndc_coords = np.zeros((pixels.shape[0], 4), dtype="float32")
        ndc_coords[:,0] = (pixels[:,0] / w * 2) - 1
        # ndc_coords[:,1] = (pixels[:,1] / h * 2) - 1
        # flip Y axis direction because we have top left origin at image
        # and centric origin in NDC space
        ndc_coords[:,1] = 1 - (pixels[:,1] / h * 2)
        ndc_coords[:,2] = -1
        ndc_coords[:,3] = 1

        return ndc_coords

    def draw_lines(self, points: np.ndarray, color: Tuple[int, int, int],
                   width :int=1) -> None:
        pixels = self.ndc_coord_to_pixel(points)
        points = [tuple(el) for el in pixels]
        self.d.line(points, width=width, fill=color)

    def draw_points(self, points: np.ndarray, color: Tuple[int, int, int],
                    size: int=2) -> None:
        pixels = self.ndc_coord_to_pixel(points)
        # points = [tuple(el) for el in pixels]
        for p in pixels:
            rec_min = p[:2]-size
            rec_max = p[:2]+size
            rec = [p[0]-size, p[1]-size, p[0]+size, p[1]+size]
            self.d.rectangle(rec, fill=color)


