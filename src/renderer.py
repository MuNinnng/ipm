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

    def coords_to_pixels(self, points: np.ndarray) -> np.ndarray:
        """Convert data from image space to screen space."""

        w,h = self.image.size
        pixels = np.copy(points)
        pixels[:,0] = (pixels[:,0] + 1)*w/2
        # FIXME: it looks like Y axis should be flipped
        pixels[:,1] = (pixels[:,1] + 1)*h/2
        pixels = pixels[:,:2].astype(int)
        return pixels

    def draw_lines(self, points: np.ndarray, color: Tuple[int, int, int],
                   width :int=1) -> None:
        pixels = self.coords_to_pixels(points)
        points = [tuple(el) for el in pixels]
        self.d.line(points, width=width, fill=color)

    def draw_points(self, points: np.ndarray, color: Tuple[int, int, int],
                    size: int=2) -> None:
        pixels = self.coords_to_pixels(points)
        # points = [tuple(el) for el in pixels]
        for p in pixels:
            rec_min = p[:2]-size
            rec_max = p[:2]+size
            rec = [p[0]-size, p[1]-size, p[0]+size, p[1]+size]
            self.d.rectangle(rec, fill=color)


if __name__ == "__main__":
    from matplotlib import pyplot as plt

    x_axis = np.array([
        [0,0,0,1],
        [.5,0,0,1],
        [1,0,0,1],
        [0,1,0,1],
        ])


    vp = Viewport((500,500))

    test_data = np.array([
        [1,0,0]
        ])
    vp.draw_points(x_axis, color=(0,0,255), size=2)

    plt.imshow(vp.image)
    plt.show()

