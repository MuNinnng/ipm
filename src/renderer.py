import numpy as np
from PIL import Image, ImageDraw


class Viewport(object):
    def __init__(self, size):
        self.size = size
        self.data = np.zeros(size)
        self.image = Image.new('RGB', size, color=(255,255,255))
        self.d = ImageDraw.Draw(self.image)

    def coords_to_pixels(self, points):
        w,h = self.data.shape
        """Convert data from image space to screen space."""
        pixels = np.copy(points)
        pixels[:,0] = (pixels[:,0] + 1)*w/2
        pixels[:,1] = (pixels[:,1] + 1)*h/2
        pixels = pixels[:,:2].astype(int)
        return pixels

    def draw_lines(self, points, color, width=1):
        pixels = self.coords_to_pixels(points)
        points = [tuple(el) for el in pixels]
        self.d.line(points, width=width, fill=color)

    def draw_points(self, points, color, width=1):
        pixels = self.coords_to_pixels(points)
        points = [tuple(el) for el in pixels]
        self.d.point(points, fill=color)


if __name__ == "__main__":
    from matplotlib import pyplot as plt

    x_axis = np.array([
        [0,0,0,1],
        [.5,0,0,1],
        ])


    vp = Viewport((500,500))

    test_data = np.array([
        [1,0,0]
        ])
    vp.draw_line(x_axis, color=(0,0,255), width=1)

    plt.imshow(vp.image)
    plt.show()

