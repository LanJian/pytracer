class Sphere:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    # alias attributes
    @property
    def c(self):
        self.center

    @property
    def r(self):
        self.radius

    def intersection(self, ray):
        pass

    def normal(self, point):
        pass
