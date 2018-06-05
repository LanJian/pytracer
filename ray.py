class Ray:
    def __init__(self, position, direction):
        self.p = position
        self.d = direction

    def __str__(self):
        return f'R {self.p} {self.d}'
