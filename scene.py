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
        pixels = [[(255, 255, 255) for u in range(self.width)]
                  for v in range(self.height)]
        d = (self.width / 2) / math.tan(math.radians(self.fov / 2))
        for u in range(self.width):
            for v in range(self.height):
                vector = (self.camera.view * d
                          + self.camera.side * (u - (self.width - 1) / 2)
                          + self.camera.up * ((self.height - 1) / 2 - v))
                ray = Ray(self.camera.position, vector.normalize())
                for obj in self.objects:
                    if obj.intersection(ray):
                        pixels[v][u] = (0, 0, 0)

        return pixels
