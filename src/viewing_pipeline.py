# -*- coding: utf-8 -*-


class Pipeline(object):
    def to_image_space(self):
        pass

    def project(self, points):
        # convert objects to camera view
        res = camera_transform()
        # convert to perspective view
        res = to_image_space(res)
        # convert to screen view(projection)
        res = to_screen_space(res)