from PIL import Image

from vector import Vector
from point import Point
from camera import Camera
from scene import Scene
from sphere import Sphere
from color import Color
from light import Light
from phong import Phong

camera = Camera(Point.ORIGIN - Vector.K * 10, Vector.J, Vector.K)
scene = Scene(camera, 800, 600, 70, Color.BLACK)

lights = [
    Light(Point(0, 100, 0), Color.WHITE * 0.1, Color.WHITE, Color.WHITE),
    Light(Point(-100, 30, -20), Color.WHITE * 0.1, Color.RED, Color(255, 200, 200))
]

objects = [
    Sphere(
        Point(0, -10, 4),
        8,
        Phong(
            Color(100, 100, 150),
            Color(100, 100, 150),
            Color.WHITE,
            50,
            0.5,
            reflect_bg=True
        )
    ),
    Sphere(
        Point(-2, 2, 4),
        3,
        Phong(
            Color(60, 250, 60),
            Color(60, 250, 60),
            Color.WHITE,
            50,
            0.3
        )
    ),
    Sphere(
        Point(5, 0, 2),
        2,
        Phong(
            Color(250, 60, 60),
            Color(250, 60, 60),
            Color.WHITE,
            20,
            0.5
        )
    ),
    Sphere(
        Point(0, 4, 0),
        1,
        Phong(
            Color.ORANGE,
            Color.ORANGE,
            Color.WHITE,
            30,
            0.3
        )
    )
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

