def step(x, n):  # x is starting guess, trying to find squareroot(N)
    return (x+n/x)/2


def sqrt(n):
    x = 30.0
    for i in range(0,10):
        xi = x
        x = step(x, n)
        if abs(xi-x) < 0.0001:
            #print "Took %r rounds to come to a solution." % i
            break
    return x

n = 125348

"""
print "My squareroot: %r" % sqrt(N)
print "Math sqrt(): %r" % math.sqrt(N)
"""


