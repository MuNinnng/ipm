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

    def pixel_to_ndc(self, pixels, viewport_size):
        """Convert pixel values to Normalized Device Coordinates."""
        w,h = viewport_size

        ndc_coords = np.zeros((pixels.shape[0], 4), dtype="float32")
        ndc_coords[:,0] = (pixels[:,0] / w * 2) - 1
        ndc_coords[:,1] = (pixels[:,1] / h * 2) - 1
        ndc_coords[:,2] = -1
        ndc_coords[:,3] = 1

        return ndc_coords

    def unproject(self, pixels, viewport_size):
        # the Normalized Device Coordinates (NDC).
        # turn pixel value to Image space coordinates
        ndc_near_coords = self.pixel_to_ndc(pixels, viewport_size)
        ndc_far_coords = np.copy(ndc_near_coords)
        # set pixel point at far plane
        ndc_far_coords[:, 2] = 1

        perspective_mat = self.transform.perspective_matrix
        view_mat = self.transform.get_camera_matrix()
        # FIXME does not work for some reason
        unproject_mat = np.linalg.inv(perspective_mat @ view_mat)

        new_near_points = ndc_near_coords @ unproject_mat
        new_near_points = self.transform.homogenus_to_world(new_near_points)

        new_far_points = ndc_far_coords @ unproject_mat
        new_far_points = self.transform.homogenus_to_world(new_far_points)

        print(new_near_points)
        print(new_far_points)


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

    pixels = np.array([
        [25,25]
        ])


    pl = Pipeline()
    pl.transform.set_camera([0,0,50])
    # projected_p = pl.project(square)

    unprojected = pl.unproject(pixels, (50,50))

    # vp = Viewport((100,200))
    # vp.render(projected_p)

    # print(vp.data)

    # plt.imshow(vp.data)
    # plt.show()