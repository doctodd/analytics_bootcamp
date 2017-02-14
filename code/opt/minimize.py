import numpy as np
from pylab import imshow, plot

def minimize(f, B0, eta, h, precision):
    #print 'Performing minimization. Please stand by...'
    trace = []
    trace.append(B0)  # Add the starting position
    B = B0
    #print 'Starting at location', B0
    steps = 0
    while True:
        Blast = B
        steps += 1
        if steps % 10 == 0: # only capture every 10th value
            trace.append(B)
            #print B
        Cprime = (f((B[0] + h, B[1])) - f(B), f((B[0], B[1] + h)) - f(B))
        B = (B[0] - eta[0]*Cprime[0], B[1] - eta[1]*Cprime[1])

        delta = f(B) - f(Blast)
        if abs(delta) < precision and delta > 0:
            break

    #print 'Found', B, 'in', steps, 'steps.'
    #print 'Expected (-36.000625, 15.484375).'
    return (B, steps, trace)
