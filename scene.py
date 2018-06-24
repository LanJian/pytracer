import math

from ray import Ray
from color import Color


class Scene:
    DEPTH = 3

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
                pixels[v][u] = self.trace(ray, self.DEPTH)

        return pixels

    def trace(self, ray, depth=1, exclude=None, miss_color=None):
        if miss_color is None:
            miss_color = self.background

        if depth == 0:
            return miss_color

        closest = self.closest_intersection(ray, exclude=exclude)
        if not closest:
            return miss_color

        obj = closest['obj']
        point = closest['point']
        n = obj.normal(point)

        mat = obj.material
        ka = mat.ambient
        kd = mat.diffuse
        ks = mat.specular
        a = mat.shininess
        ref = mat.reflectance
        trans = mat.transmittance

        vv = (-ray.d).normalize()
        h = (vv * n) * 2 * n - vv

        # local color
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

            local_color += ka * la
            if l * n > 0:
                local_color += kd * (l * n) * ld
            if r * vv > 0:
                local_color += ks * (r * vv)**a * ls

        if ref == 0 and trans == 0:
            return local_color

        # relected color
        reflected_color = Color.BLACK
        reflected_ray = Ray(point, h)
        miss_color = self.background if mat.reflect_bg else local_color
        reflected_color = self.trace(
            reflected_ray, depth - 1, exclude=obj, miss_color=miss_color)

        # transmitted color
        refracted_color = Color.BLACK
        ft = 0
        fr = 1
        if trans > 0:
            epsilon = 0.0001
            # refract into object
            refraction = ray.d.refract(n, mat.ior)
            refracted_d = refraction['t']
            # fresnel
            ft = refraction['ft']
            fr = 1 - ft
            if refracted_d is not None:
                refracted_ray = Ray(point + refracted_d * epsilon, refracted_d)
                refracted_color = self.trace(refracted_ray, depth - 1)

        # adjust reflectance and transmittance with fresnel
        ref = ref + fr * trans
        trans = ft * trans
        return reflected_color * ref\
            + refracted_color * trans\
            + local_color * (1 - ref - trans) * fr

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
