__author__ = 'Todd'


from filter import *


def avg(data):
    # Takes a list of data and return the average value
    return sum(data)/len(data)


img = open(sys.argv)
img.show()
img = filter(img, avg)
img.show()