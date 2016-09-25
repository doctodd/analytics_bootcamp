__author__ = 'Todd'

import sys
from PIL import Image

if len(sys.argv) != 2:
    print '$ python view.py imagefilename'
    sys.exit(1)

filename = sys.argv[1] # get the argument passed to us by the OS
img = Image.open(filename) # load the file specified on the command line
img = img.convert('L') # grayscale
img.show()