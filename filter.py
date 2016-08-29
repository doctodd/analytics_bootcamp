import sys
from PIL import Image

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


def open(argv):
    if len(argv)<=1:
        print "missing image filename"
        sys.exit(1)
    img = Image.open(argv[1])
    img = img.convert("L")  # make greyscale if not already (luminance)
    return img


def filter(image, f):
    imgdup = image.copy()
    width, height = image.size
    m = image.load()
    w = imgdup.load()

    for y in range(height):
        for x in range(width):
            w[x,y] = f(region3x3(image, x, y))

    return imgdup
