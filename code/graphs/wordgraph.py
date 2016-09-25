from graph import *
import sys

def gml2adjlist(G):
    # todo Create the function
    print G.node

    words = collections.OrderedDict()  # keep stuff in order read from GML
    return words


if len(sys.argv)<=1:
    print "missing gml filename"
    sys.exit(1)
filename = sys.argv[1]
gmlfile = open(filename)

alist = gml2adjlist(gmlfile)

dot = gendot(alist)
print dot