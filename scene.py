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
        pixels = []
        d = (self.width / 2) / math.tan(math.radians(self.fov / 2))
        for u in range(self.width):
            row = []
            pixels.append(row)
            for v in range(self.height):
                vector = (self.camera.view * d
                          + self.camera.side * (u - (self.width - 1) / 2)
                          + self.camera.up * ((self.height - 1) / 2 - v))
                ray = Ray(self.camera.position, vector.normalize())
                print(ray)
