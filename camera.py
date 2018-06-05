class Camera:
    def __init__(self, up, side, fov):
        self.up = up
        self.side = side
        self.fov = fov
        self.forward = up.cross(side)
