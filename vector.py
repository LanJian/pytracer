import math
import numbers

class Vector:
    def __init__(self, *elements):
        self.elements = elements
        # convenience attributes for R^2 and R^3
        self.x = self[0]
        self.y = self[1]
        self.z = self[2]

    def __getitem__(self, index):
        return self.elements[index]

    def __add__(self, other):
        return Vector(*[a + b for a, b in zip(self.elements, other.elements)])

    def __sub__(self, other):
        return Vector(*[a - b for a, b in zip(self.elements, other.elements)])

    def __mul__(self, other):
        if isinstance(other, numbers.Number):
            return Vector(*[e * other for e in self.elements])
        else:
            return sum([a * b for a, b in zip(self.elements, other.elements)])

    def __rmul__(self, other):
        return self * other

    def __neg__(self):
        return Vector.ZERO - self

    # magnitude
    def __abs__(self):
        return math.sqrt(sum([e * e for e in self.elements]))

    def cross(self, other):
        u = self
        v = other
        return Vector(
            u[1]*v[2] - u[2]*v[1],
            u[2]*v[0] - u[0]*v[2],
            u[0]*v[1] - u[1]*v[0]
        )

    def normalize(self):
        mag = abs(self)
        return Vector(*[e / mag for e in self.elements])

    def refract(self, n, ior):
        i = self
        eta1 = 1
        eta2 = ior
        eta = eta1 / eta2
        cos1 = n * i
        sin2 = eta1 / eta2 * math.sqrt(1 - cos1 * cos1)
        cos2 = math.sqrt(1 - sin2 * sin2)

        if cos1 < 0:  # ray is going from air to denser material
            cos1 = -cos1
        else:
            n = -n
            eta = eta2 / eta1


        k = 1 - eta * eta * (1 - cos1 * cos1)
        if k < 0:  # total internal reflection
            # transmitted light is 0
            return {'ft': 0, 't': None}

        fr_parallel = (
            (eta2 * cos1 - eta1 * cos2)
            / (eta2 * cos1 + eta1 * cos2)
        )**2
        fr_perpendicular = (
            (eta1 * cos2 - eta2 * cos1)
            / (eta1 * cos2 + eta2 * cos1)
        )**2

        fr = (fr_parallel + fr_perpendicular) / 2

        c2 = math.sqrt(k)
        t = eta * (i  + cos1 * n) - n * c2
        return {'ft': 1 - fr, 't': t.normalize()}

    def __str__(self):
        return f'V{self.elements}'

Vector.ZERO = Vector(0, 0, 0)
Vector.I = Vector(1, 0, 0)
Vector.J = Vector(0, 1, 0)
Vector.K = Vector(0, 0, 1)
