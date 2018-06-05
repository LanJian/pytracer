from vector import Vector

class Point:
    def __init__(self, *elements):
        self.elements = elements
        # convenience attributes for R^2 and R^3
        self.x = self[0]
        self.y = self[1]
        self.z = self[2]

    def __getitem__(self, index):
        return self.elements[index]

    def __add__(self, other):
        return Point(*[a + b for a, b in zip(self.elements, other.elements)])

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Point(*[a - b for a, b in
                zip(self.elements, other.elements)])
        else:
            return Vector(*[a - b for a, b in
                zip(self.elements, other.elements)])

    def __str__(self):
        return f'P{self.elements}'
