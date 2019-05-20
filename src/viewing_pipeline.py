# -*- coding: utf-8 -*-
import numpy as np

from matrix import Transform


class Pipeline(object):
    def __init__(self):
        self.transform = Transform()

    def camera_transformation(self, points):
        cam_matrix = self.transform.get_camera_matrix()
        return points @ cam_matrix

    def to_image_space(self, points):
        new_points = points @ self.transform.perspective_matrix
        new_points = self.transform.homogenus_to_world(new_points)
        return new_points

    def project(self, points):
        # convert objects to camera view
        res = self.camera_transformation(points)
        # # convert to perspective view
        res = self.to_image_space(res)
        return res
        # # convert to screen view(projection)
        # res = to_screen_space(res)

    def upproject(self, pixels):
        w,h = self.viewport.size
        # the Normalized Device Coordinates (NDC).
        # turn pixel value to Image space coordinates
        ndc_coords = np.zeros((pixels.shape[0], 4))
        ndc_coords[:,0] = (ndc_coords[:,0] / w * 2) - 1
        ndc_coords[:,1] = (ndc_coords[:,1] / h * 2) - 1
        ndc_coords[:,2] = 0
        ndc_coords[:,3] = 1


        pass


if __name__ == "__main__":
    from matplotlib import pyplot as plt
    from renderer import Viewport

    square = np.array([
        [-1,-1,1,1],
        [-1,1,1,1],
        [1,1,1,1],
        [1,-1,1,1],
        [-1,-1,1,1],
        ])

    square = np.array([
        [-3,-1,1,1],
        [-1,1,1,1],
        [1,1,1,1],
        [1,-1,1,1],
        [-1,-1,0,1],
        [-1,1,0,1],
        [1,1,0,1],
        [1,-1,0,1],
        ])

    pl = Pipeline()
    pl.transform.set_camera([0,0,50])
    projected_p = pl.project(square)

    vp = Viewport((100,200))
    vp.render(projected_p)

    print(vp.data)

    plt.imshow(vp.data)
    plt.show()