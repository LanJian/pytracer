class Camera:
    def __init__(self, position, up, view):
        self.position = position
        self.up = up
        self.view = view
        self.side = up.cross(view)

    @property
    def p(self):
        return self.position
