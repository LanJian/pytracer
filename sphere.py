import math


class Sphere:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    # alias attributes
    @property
    def c(self):
        return self.center

    @property
    def r(self):
        return self.radius

    def intersection(self, ray):
        o = ray.p
        l = ray.d
        c = self.c
        r = self.r

        discriminant = (l * (o - c))**2 - abs(o - c)**2 + r**2
        if discriminant < 0:
            return None

        sqrt_disc = math.sqrt(discriminant)
        d1 = -(l * (o - c)) + sqrt_disc
        d2 = -(l * (o - c)) - sqrt_disc

        if d1 < 0 and d2 < 0:
            return None

        d = min([d1, d2])

        if d1 < 0:
            d = d2

        if d2 < 0:
            d = d1

        return {'point': o + d * l, 't': d}

    def normal(self, point):
        pass
