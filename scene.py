import math

from ray import Ray
from color import Color


class Scene:
    def __init__(self, camera, width, height, fov, background):
        self.objects = []
        self.lights = []
        self.camera = camera
        self.width = width
        self.height = height
        self.fov = fov
        self.background = background

    def add(self, object):
        self.objects.append(object)

    def add_light(self, light):
        self.lights.append(light)

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
                pixels[v][u] = self.trace(ray)

        return pixels

    def trace(self, ray, depth=1):
        if depth == 0:
            return self.background

        closest = self.closest_intersection(ray)
        if not closest:
            return self.background

        obj = closest['obj']
        point = closest['point']
        n = obj.normal(point)

        mat = obj.material
        ka = mat.ambient
        kd = mat.diffuse
        ks = mat.specular
        a = mat.shininess

        local_color = Color.BLACK

        for light in self.lights:
            la = light.ambient
            ld = light.diffuse
            ls = light.specular
            l = (light.position - point).normalize()

            obstructor = self.closest_intersection(
                Ray(point, l), exclude=obj)

            if obstructor is not None:
                continue

            r = (l * n) * 2 * n - l
            view = (-ray.d).normalize()

            local_color += ka * la
            if l * n > 0:
                local_color += kd * (l * n) * ld
            if r * view > 0:
                local_color += ks * (r * view)**a * ls

        return color

    def closest_intersection(self, ray, exclude=None):
        intersections = [
            o.intersection(ray) for o in self.objects if o is not exclude
        ]
        intersections = [x for x in intersections if x is not None]

        # miss
        if not intersections:
            return None

        # hit
        return min(intersections, key=lambda x: x['t'])
