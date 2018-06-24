from PIL import Image

from vector import Vector
from point import Point
from camera import Camera
from scene import Scene
from sphere import Sphere
from color import Color
from light import Light
from phong import Phong
from plane import Plane


camera = Camera(Point(0, -8, -20), Vector.J, Vector.K)
scene = Scene(camera, 800, 600, 70, Color.WHITE * 0.03)

lights = [
    Light(Point(0, 100, 0), Color.WHITE * 0.1, Color.WHITE, Color.WHITE),
    Light(Point(-100, 50, -80), Color.WHITE * 0.1,
          Color(255, 100, 100), Color(255, 200, 200))
]

objects = [
    Plane(
        Point(0, -8.5, 0),
        Vector.J,
        Phong(
            Color(56, 0, 3),
            Color(56, 0, 3),
            Color.WHITE,
            50,
            transmittance=0.8,
            ior=1.3,
            reflect_bg=True
        )
    ),
    Sphere(
        Point(0, 0, 15),
        8,
        Phong(
            Color(100, 100, 150),
            Color(100, 100, 150),
            Color.WHITE,
            50,
        )
    ),
    Sphere(
        Point(-15, -2, 12),
        5,
        Phong(
            Color(156, 174, 95),
            Color(156, 174, 95),
            Color.WHITE,
            15,
        )
    ),
    Sphere(
        Point(15, -1, 10),
        3,
        Phong(
            Color(136, 54, 117),
            Color(136, 54, 117),
            Color.WHITE,
            80,
        )
    ),
    Sphere(
        Point(-4, -3, 0),
        3,
        Phong(
            Color.BLACK,
            Color.BLACK,
            Color.BLACK,
            50,
            transmittance=0.8,
            ior=1.05,
            reflect_bg=True
        )
    ),
    Sphere(
        Point(3, -5, -4),
        2,
        Phong(
            Color.BLACK,
            Color.BLACK,
            Color.BLACK,
            50,
            transmittance=0.8,
            ior=1.5,
            reflect_bg=True
        )
    ),
]


for o in objects:
    scene.add(o)
for l in lights:
    scene.add_light(l)

result = scene.render()

img = Image.new('RGB', (scene.width, scene.height), tuple(scene.background))
pixels = img.load()

for u in range(img.size[0]):
    for v in range(img.size[1]):
        pixels[u, v] = tuple(result[v][u])

img.save('output.png')
