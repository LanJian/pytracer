class Camera:
    def __init__(self, up, view, fov):
        self.up = up
        self.view = view
        self.fov = fov
        self.side = up.cross(view)
