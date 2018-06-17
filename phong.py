from color import Color


class Phong:
    def __init__(self, ambient, diffuse, specular, shininess,
                 reflectance=0, reflect_bg=False,
                 transmittance=0, ior=1):
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.shininess = shininess

        self.reflectance = reflectance
        self.reflect_bg = reflect_bg

        self.transmittance = transmittance
        self.ior = ior  # index of refraction


Phong.mirror = Phong(
    Color.BLACK, Color.BLACK, Color.WHITE, 50, 0.8, reflect_bg=True)
