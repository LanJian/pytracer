import math

from ray import Ray

class Scene:
    def __init__(self, camera, width, height, fov):
        self.objects = []
        self.camera = camera
        self.width = width
        self.height = height
        self.fov = fov

    def add(self, object):
        self.objects.append(object)

    def raytrace(self):
        rays = []
        d = (self.width / 2) / math.tan(math.radians(self.fov / 2))
        for i in self.width:
            for j in self.height:
                vector = (self.camera.view * d
                          + self.camera.side * (self.width / 2 - i)
                          + self.camera.up * (self.height / 2 - j))
                ray = Ray(self.camera.position, vector)
                print(ray)
                rays.append(ray)
