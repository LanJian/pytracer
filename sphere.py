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

        term = (l * (o - c))**2 - abs(o - c)**2 + r**2
        if term < 0:
            return False
        return True

    def normal(self, point):
        pass
