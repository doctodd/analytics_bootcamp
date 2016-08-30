__author__ = 'Todd'

import sys
from PIL import Image


def avg(data):
    # Takes a list of data and return the average value
    return sum(data)/len(data)


def getpixel(image, x, y):
    # Takes an image and coordinate, then returns the value of the pixel at that coordinate.
    m = image.load()    # m is now a 2D array with a pixel at each location
    width, height = image.size
    # But first check to make sure x and y are not off the edge of the image.
    if x < 0:
        x = 0
    if x >= width:
        x = width - 1
    if y < 0:
        y = 0
    if y >= height:
        y = height - 1
    return m[x, y]

def region3x3(image, x, y):
    # From a given pixel, return a list of the pixel and all the neighboring pixels
    me = getpixel(image, x, y)
    N = getpixel(image, x, y - 1)
    NE = getpixel(image, x + 1, y - 1)
    E = getpixel(image, x + 1, y)
    SE = getpixel(image, x + 1, y + 1)
    S = getpixel(image, x, y + 1)
    SW = getpixel(image, x - 1, y + 1)
    W = getpixel(image, x - 1, y)
    NW = getpixel(image, x - 1, y - 1)

    a = [me, N, NE, E, SE, S, SW, W, NW]
    return a

# define your blur function here
def blur(image):
    imgdup = image.copy()
    width, height = image.size
    m = image.load()
    w = imgdup.load()

    for y in range(height):
        for x in range(width):
            w[x,y] = avg(region3x3(image, x, y))

    return imgdup


if len(sys.argv)<=1:
    print "missing image filename"
    sys.exit(1)
filename = sys.argv[1]
img = Image.open(filename)
img = img.convert("L")
img.show()

# call your blur function here
blurred = blur(img)

blurred.show()