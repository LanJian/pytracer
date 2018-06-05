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

    # magnitude
    def __abs__(self):
        return math.sqrt(sum([e * e for e in self.elements]))

    def cross(self, other):
        pass

    def normalize(self):
        mag = abs(self)
        return Vector(*[e / mag for e in self.elements])

    def __str__(self):
        return f'V{self.elements}'
