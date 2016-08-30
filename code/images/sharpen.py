__author__ = 'Todd'

from filter import *


def laplace(data):
    # Takes a list of data, and returns a value based on the Laplacian (
    return data[1] + data[3] + data[5] + data[7] - 4 * data[0]


def minus(A, B):
    # Takes 2 images A and B, and returns image A-B, note: assumes images are the same size
    width, height = A.size
    m = A.load()
    n = B.load()

    for y in range(height):
        for x in range(width):
            m[x,y] = m[x,y] - n[x,y]

    return A



img = open(sys.argv)
img.show()
edges = filter(img, laplace)
sharpened = minus(img, edges)
sharpened.show()
