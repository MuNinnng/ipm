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
        print("in",points)
        camera_mat = self.transform.get_camera_matrix()
        perspective_mat = self.transform.perspective_matrix

        project_mat = camera_mat @ perspective_mat
        # project_mat = perspective_mat
        project_mat = self.transform.view_matrix
        # project_mat = perspective_mat @ camera_mat
        # convert objects to camera view
        # res = self.camera_transformation(points)
        # # convert to perspective view
        # res = self.to_image_space(res)

        res = points @ project_mat
        # res = project_mat @
        print("out1",res)

        res = self.transform.homogenus_to_world(res)
        print("out2",res)
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
        unproject_mat = np.linalg.inv(view_mat @ perspective_mat)

        new_near_points = ndc_near_coords @ unproject_mat
        new_near_points = self.transform.homogenus_to_world(new_near_points)

        new_far_points = ndc_far_coords @ unproject_mat
        new_far_points = self.transform.homogenus_to_world(new_far_points)

        vec = new_far_points - new_near_points

        print(vec)
        # print(new_favecr_points)


if __name__ == "__main__":
    from matplotlib import pyplot as plt
    from renderer import Viewport
    
    origin = np.array([
        [0,0,0,1],
        ])

    x_axis = np.array([
        [0,0,0,1],
        [1,0,0,1],
        ])
    y_axis = np.array([
        [0,0,0,1],
        [0,1,0,1],
        ])
    z_axis = np.array([
        [0,0,0,1],
        [0,0,1,1],
        ])


    square = np.array([
        [0,0],
        [0,1],
        [1,1],
        [1,0],
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
        [50,50]
        ])


    pl = Pipeline()
    pl.transform.set_camera([1, 0, 100])
    # projected_p = pl.project(square)
    projected_origin = pl.project(origin)
    # projected_x_axis = pl.project(x_axis)
    # projected_y_axis = pl.project(y_axis)
    # projected_z_axis = pl.project(z_axis)
    # print(projected_p)

    # unprojected = pl.unproject(pixels, (50,50))

    vp = Viewport((50,50))
    # vp.render(projected_p)
    vp.render(projected_origin, color=255)
    # vp.render(projected_x_axis, color=100)
    # vp.render(projected_z_axis, color=50)

    # print(vp.data)

    plt.imshow(vp.data)
    plt.show()


 #    [[-0.13928156 -0.04642719  0.94616159]
 # [-0.04642719  0.04642719  0.94616159]
 # [ 0.04642719  0.04642719  0.94616159]
 # [ 0.04642719 -0.04642719  0.94616159]
 # [-0.04733752 -0.04733752  0.94502735]
 # [-0.04733752  0.04733752  0.94502735]
 # [ 0.04733752  0.04733752  0.94502735]
 # [ 0.04733752 -0.04733752  0.94502735]]