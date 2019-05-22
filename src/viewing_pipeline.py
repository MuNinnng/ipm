# -*- coding: utf-8 -*-
import numpy as np

from transform import Transform


class Pipeline(object):
    def __init__(self, viewport):
        self.transform = Transform()
        self.viewport = Viewport(viewport)

    def camera_transformation(self, points):
        cam_matrix = self.transform.get_camera_matrix()
        return points @ cam_matrix

    def to_image_space(self, points):
        new_points = points @ self.transform.perspective_matrix
        new_points = self.transform.homogenus_to_world(new_points)
        return new_points

    def project(self, points):
        points = self.transform.world_to_homogenus(points)

        camera_mat = self.transform.get_camera_matrix()
        perspective_mat = self.transform.perspective_matrix

        project_mat = camera_mat @ perspective_mat
        # project_mat = perspective_mat
        # project_mat = self.transform.view_matrix
        # project_mat = perspective_mat @ camera_mat
        # convert objects to camera view
        # res = self.camera_transformation(points)
        # # convert to perspective view
        # res = self.to_image_space(res)

        res = points @ project_mat
        # res = project_mat @
        res = self.transform.homogenus_to_world(res)
        return res
        # # convert to screen view(projection)
        # res = to_screen_space(res)

    def pixel_to_ndc(self, pixels, viewport_size):
        """Convert pixel values to Normalized Device Coordinates."""
        w,h = viewport_size

        ndc_coords = np.zeros((pixels.shape[0], 4), dtype="float32")
        ndc_coords[:,0] = (pixels[:,0] / w * 2) - 1
        # ndc_coords[:,1] = (pixels[:,1] / h * 2) - 1
        # flip Y axis direction because we have top left origin at image
        # and centric origin in NDC space
        ndc_coords[:,1] = 1 - (pixels[:,1] / h * 2)
        ndc_coords[:,2] = -1
        ndc_coords[:,3] = 1

        return ndc_coords

    def unproject(self, pixels):
        # the Normalized Device Coordinates (NDC).
        # turn pixel value to Image space coordinates
        ndc_near_coords = self.pixel_to_ndc(pixels, self.viewport.size)
        ndc_far_coords = np.copy(ndc_near_coords)
        # set pixel point at far plane
        ndc_far_coords[:, 2] = 1

        perspective_mat = self.transform.perspective_matrix
        view_mat = self.transform.get_camera_matrix()
        # FIXME does not work for some reason
        unproject_mat = np.linalg.inv(view_mat @ perspective_mat)
        # unproject_mat = view_mat @ perspective_mat
        # unproject_mat = np.linalg.inv(self.transform.view_matrix @ perspective_mat)
        # unproject_mat = np.linalg.inv(perspective_mat @ view_mat)

        new_near_points = ndc_near_coords @ unproject_mat
        new_near_points = self.transform.homogenus_to_world(new_near_points)

        new_far_points = ndc_far_coords @ unproject_mat
        new_far_points = self.transform.homogenus_to_world(new_far_points)


        # print(new_near_points)
        # print(new_far_points)
        vec = new_far_points - new_near_points
        return new_near_points, new_far_points
        # print("vec", vec)



    def draw(self, objects):
        for obj in objects:
            if obj["type"] == "line":
                projected = self.project(obj["geom"])
                self.viewport.draw_lines(projected, color=obj["color"], width=obj["width"])
            if obj["type"] == "point":
                projected = self.project(obj["geom"])
                self.viewport.draw_points(projected, color=obj["color"], size=obj["size"])

    def show(self):
        plt.imshow(self.viewport.image)
        # inverse Y axis because of image coord system
        plt.gca().invert_yaxis()
        plt.show()

        # print(new_favecr_points)


if __name__ == "__main__":
    from matplotlib import pyplot as plt
    from renderer import Viewport
    import geometry as g
    from plane_intersection import ray_plane_intersection


    pl = Pipeline(viewport=(500,500))
    # pl.transform.set_camera([0, 0, -10])
    # pl.transform.rotate_y(10)
    pl.transform.set_translation(y=0,x=0,z=-5)

    screen_point = np.array([
        [250,250],
        [350,250],
        # [250,0],
        [250,300],
        ])

    n_points, f_points = pl.unproject(screen_point)
    zy_plane_norm = np.array([1,0,0])
    zx_plane_norm = np.array([0,1,0])
    xy_plane_norm = np.array([0,0,1])
    plane_point = np.array([0,0,0])

    test = [
        {"geom": f_points, "type": "point", "color":(255,0,0), "size":3},
    ]

    # calc intersection
    # inter = ray_plane_intersection(n_points, f_points, plane_point, xy_plane_norm)
    # pl.viewport.draw_points(inter, color=(255,0,0), size=3)
    # print(inter)
    pl.draw(g.axis)
    pl.draw(test)
    pl.show()
   
