from PIL import Image

from vector import Vector

# PIL accesses images in Cartesian co-ordinates, so it is Image[columns, rows]
img = Image.new( 'RGB', (255,255), "black") # create a new black image
pixels = img.load() # create the pixel map

for i in range(img.size[0]):    # for every col:
    for j in range(img.size[1]):    # For every row
        pixels[i,j] = (i, j, 0) # set the colour accordingly

img.save('output.png')

# testing vector stuff
v1 = Vector(2, 0, 0)
v2 = Vector(1, 2, 0)
print(v1[0])
print(v1[1])
print(v1[2])
print(v1 + v2)
print(v1 - v2)
print(v1 * v2)
print(v1 * 10)
print(abs(Vector(3, 4, 0)))
print(v2.normalize())
print(abs(v2.normalize()))
