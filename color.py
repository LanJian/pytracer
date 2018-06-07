import numbers


class Color:
    def __init__(self, r, g, b):
        self.r = round(r)
        self.g = round(g)
        self.b = round(b)
        self.clamp()

    # make this class an iterable so we can convert to tuple
    def __getitem__(self, key):
        return [self.r, self.g, self.b][key]

    def __add__(self, other):
        return Color(
            self.r + other.r,
            self.g + other.g,
            self.b + other.b
        )

    def __iadd__(self, other):
        return self + other

    def __mul__(self, other):
        if isinstance(other, numbers.Number):
            return Color(
                self.r * other,
                self.g * other,
                self.b * other
            )

        return Color(
            self.r / 255 * other.r,
            self.g / 255 * other.g,
            self.b / 255 * other.b,
        )

    def __str__(self):
        return f'C{(self.r, self.g, self.b)}'

    def clamp(self):
        self.r = max([min([self.r, 255]), 0])
        self.g = max([min([self.g, 255]), 0])
        self.b = max([min([self.b, 255]), 0])


Color.BLACK = Color(0, 0, 0)
Color.WHITE = Color(255, 255, 255)
Color.RED = Color(255, 0, 0)
Color.GREEN = Color(0, 255, 0)
Color.BLUE = Color(0, 0, 255)
