class Plane:
    def __init__(self, p, n, material):
        self.p = p
        self.n = n
        self.material = material

    def intersection(self, ray):
        l = ray.d
        n = self.n
        l0 = ray.p
        p0 = self.p

        if l * n == 0:
            # ray is parallel to plane, either outside or inside the plane,
            #   but in either case, we can't see it
            return None

        d = (p0 - l0) * n / (l * n)

        if d < 0:
            # intersection is behind us, we can't see it
            return None

        return {'point': l0 + d * l, 't': d, 'obj': self}

    def normal(self, point):
        return self.n
