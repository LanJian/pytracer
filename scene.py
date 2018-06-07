import math

from ray import Ray
from color import Color


class Scene:
    def __init__(self, camera, width, height, fov, background):
        self.objects = []
        self.camera = camera
        self.width = width
        self.height = height
        self.fov = fov
        self.background = background

    def add(self, object):
        self.objects.append(object)

    def render(self):
        pixels = [[self.background for u in range(self.width)]
                  for v in range(self.height)]
        d = (self.width / 2) / math.tan(math.radians(self.fov / 2))
        for u in range(self.width):
            for v in range(self.height):
                vector = (self.camera.view * d
                          + self.camera.side * (u - (self.width - 1) / 2)
                          + self.camera.up * ((self.height - 1) / 2 - v))
                ray = Ray(self.camera.position, vector.normalize())
                for obj in self.objects:
                    intersection = obj.intersection(ray)
                    if intersection is not None:
                        t = intersection['t']
                        normal = obj.normal(intersection['point'])
                        pixels[v][u] = Color(
                            int((normal.x + 1) * 255 / 2),
                            int((normal.y + 1) * 255 / 2),
                            int((normal.z + 1) * 255 / 2)
                        )

        return pixels
