__author__ = 'Todd'

from filter import *


def laplace(data):
    # Takes a list of data, and returns a value based on the Laplacian (
    return data[1] + data[3] + data[5] + data[7] - 4 * data[0]


img = open(sys.argv)
img.show()
img = filter(img, laplace)
img.show()
