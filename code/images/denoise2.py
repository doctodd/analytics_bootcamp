__author__ = 'Todd'

from filter import *


def median(data):
    # Takes a list of data, sorts it, and return the median value (from position len(data)/2
    datasorted = sorted(data)
    return datasorted [len(data)/2]


img = open(sys.argv)
img.show()
img = filter(img, median)
img.show()