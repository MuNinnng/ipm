import numpy as np
from PIL import Image


class Viewport(object):
    def __init__(self, size):
        self.data = np.zeros(size)

    def coords_to_pixels(self, points):
        w,h = self.data.shape
        """Convert data from image space to screen space."""
        pixels = np.copy(points)
        pixels[:,0] = (pixels[:,0] + 1)*w/2
        pixels[:,1] = (pixels[:,1] + 1)*h/2
        pixels = pixels[:,:2].astype(int)
        return pixels

    def render(self, points):
        w, h = self.data.shape
        pixels = self.coords_to_pixels(points)

        w_range = list(range(self.data.shape[0]))
        h_range = list(range(self.data.shape[1]))
        for pixel in pixels:
            px,py = pixel
            if px == w:
                px = px - 1
            if py == h:
                py = py - 1
            if px in w_range and py in h_range:
                self.data[px, py] = 255


if __name__ == "__main__":
    from matplotlib import pyplot as plt

    vp = Viewport((50,50))

    test_data = np.array([
        [0,1,0]
        ])
    vp.render(test_data)
    print(vp.data)

    plt.imshow(vp.data)
    plt.show()

