from PIL import Image

from vector import Vector
from point import Point
from camera import Camera
from scene import Scene
from sphere import Sphere
from color import Color
from light import Light
from phong import Phong

camera = Camera(Point.ORIGIN, Vector.J, Vector.K)
scene = Scene(camera, 600, 400, 90, Color.BLACK)

lights = [
    Light(Point(0, 100, 0), Color.WHITE * 0.1, Color.WHITE, Color.WHITE),
    Light(Point(-100, 0, 0), Color.WHITE * 0.1, Color.RED, Color(255, 200, 200))
]

objects = [
    Sphere(Point(0, 0, 15), 5,
           Phong(Color(100, 100, 200), Color(100, 100, 200), Color.WHITE, 20)),
    Sphere(Point(5, 5, 20), 5,
           Phong(Color.ORANGE, Color.ORANGE, Color.WHITE, 20)),
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

