import math

from ray import Ray


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
                        pixels[v][u] = (
                            255 - int((t-18)*255/2),
                            255 - int((t-18)*255/2),
                            255 - int((t-18)*255/2)
                        )

        return pixels
