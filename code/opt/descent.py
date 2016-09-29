def minimize(f, x0, eta, h, precision):
    tracex = []
    tracex.append(x0)  # add starting position
    xi = x0
    delta = f(xi+h)-f(xi)

    #fill in
    while abs(delta) > precision:   # maybe instead use f(x) and also check that f(xi+1) is going back up
        delta = f(xi + h) - f(xi)
        xi -= eta*delta
        #print "xi:  %r, delta: %r" % (xi, delta)
        tracex.append(xi)

    return tracex
