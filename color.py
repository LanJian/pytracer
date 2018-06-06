class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        self.clamp()

    # make this class an iterable so we can convert to tuple
    def __getitem__(self, key):
        return [self.r, self.g, self.b][key]

    def clamp(self):
        self.r = max([min([self.r, 255]), 0])
        self.g = max([min([self.g, 255]), 0])
        self.b = max([min([self.b, 255]), 0])
