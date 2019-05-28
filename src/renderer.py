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
        """Convert data from image space to screen space."""

        w,h = self.size
        # reduce size because of 0 based indexing, so num 500 has 499 index
        w -= 1
        h -= 1

        pixels = np.copy(points)
        pixels[:,0] = (pixels[:,0] + 1)*w/2
        print(points[:,0])
        print(pixels[:,0])
        # (pixels[:,0] * w / 2) + 1
        # FIXME: it looks like Y axis should be flipped
        pixels[:,1] = (1 - pixels[:,1])*h/2

        print(points[:,1])
        print(pixels[:,1])
        # pixels[:,1] = (1-pixels[:,1] + 1)*h/2
        pixels = pixels[:,:2].astype(int)
        return pixels

    def pixel_to_ndc_coord(self, pixels: np.ndarray) -> np.ndarray:
        """Convert pixel values to Normalized Device Coordinates."""
        w,h = self.size

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


if __name__ == "__main__":
    from matplotlib import pyplot as plt

    x_axis = np.array([
        [-1,0,0,1],
        [0,0,0,1],
        [.5,0,0,1],
        [1,0,0,1],
        ])
    y_axis = np.array([
        [0,-1,0,1],
        [0,0,0,1],
        [0,.5,0,1],
        [0,1,0,1],
        ])


    vp = Viewport((500,500))

    test_data = np.array([
        [1,0,0]
        ])
    vp.draw_points(y_axis, color=(0,0,255), size=2)

    plt.imshow(vp.image)
    # plt.gca().invert_yaxis()
    plt.show()

