from color import Color


class Phong:
    def __init__(self, ambient, diffuse, specular,
                 shininess, reflectivity=0, reflect_bg=False):
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.shininess = shininess
        self.reflectivity = reflectivity
        self.reflect_bg = reflect_bg


Phong.mirror = Phong(
    Color.BLACK, Color.BLACK, Color.WHITE, 50, 0.8, reflect_bg=True)
