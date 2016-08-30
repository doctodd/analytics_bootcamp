__author__ = 'Todd'

import sys
from PIL import Image

# define your flip function here
def flip(image):
    imgdup = image.copy()
    width, height = image.size
    m = image.load()
    w = imgdup.load()

    for y in range(height):
        for x in range(width):
            w[x,y] = m[width-x-1,y]

    return imgdup

if len(sys.argv)<=1:
    print "missing image filename"
    sys.exit(1)
filename = sys.argv[1]
img = Image.open(filename)
img = img.convert("L")
img.show()

# call your flip function here
flipped = flip(img)

flipped.show()