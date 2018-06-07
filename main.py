from PIL import Image

from vector import Vector
from point import Point
from camera import Camera
from scene import Scene
from sphere import Sphere
from color import Color
from light import Light

camera = Camera(Point.ORIGIN, Vector.J, Vector.K)
scene = Scene(camera, 300, 200, 90, Color.BLACK)
light = Light(Point(10, 50, 10), Color.WHITE, Color.WHITE, Color.WHITE)

sphere = Sphere(Point(0, 0, 10), 5)

scene.add(sphere)

result = scene.render()

img = Image.new('RGB', (scene.width, scene.height), tuple(scene.background))
pixels = img.load()

for u in range(img.size[0]):
    for v in range(img.size[1]):
        pixels[u, v] = tuple(result[v][u])

img.save('output.png')


# v1 = Vector(2, 0, 0)
# v2 = Vector(1, 2, 0)
# print(v1[0])
# print(v1[1])
# print(v1[2])
# print(v1.x)
# print(v1.y)
# print(v1.z)
# print(v1 + v2)
# print(v1 - v2)
# print(v1 * v2)
# print(v1 * 10)
# print(abs(Vector(3, 4, 0)))
# print(v2.normalize())
# print(abs(v2.normalize()))
# print(Vector.J.cross(Vector.K))

# p1 = Point(1, 2, 3)
# p2 = Point(5, 5, 6)
# v = Vector(4, 5, 6)
# print(p1 + v)
# print(p1 - v)
# print(p2 - p1)
