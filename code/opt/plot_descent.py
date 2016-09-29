from descent import *
import matplotlib.pyplot as plt
import numpy as np
import random


def f(x):  # given cosine function
    return np.cos(3*np.pi*x)/x

# set up the figure for adding annotations
fig = plt.figure()
ax = fig.add_subplot(111)

# plot the cosine function
graphx = np.arange(.1,1.1,0.01)
graphy = f(graphx)
plt.plot(graphx,graphy)
plt.axis([0,1.1,-4,6])

# variables
ETA = 2000
STEP = 0.000001
PRECISION = 0.0000001

# run first minimization and plot
x0 = random.random()*1.1 + 0.1
tracex = minimize(f, x0, ETA, STEP, PRECISION)
tracey = [f(x) for x in tracex]
plt.plot(tracex, tracey, 'ro')  # plot red dots
plt.text(.25,.9, 'f(%f) = %r' % (tracex[-1], tracey[-1]), transform = ax.transAxes, color = "red")
plt.text(.25,.85, 'steps = %r' % len(tracex), transform = ax.transAxes, color = "red")

# run first minimization and plot
x0 = random.random()*1.1 + 0.1
tracex = minimize(f, x0, ETA, STEP, PRECISION)
tracey = [f(x) for x in tracex]
plt.plot(tracex, tracey, 'go')  # plot green dots
plt.text(.25,.75, 'f(%f) = %r' % (tracex[-1], tracey[-1]), transform = ax.transAxes, color = "green")
plt.text(.25,.7, 'steps = %r' % len(tracex), transform = ax.transAxes, color = "green")


#print "tracex: %r" % tracex
#print "# steps: %r" % len(tracex)

plt.savefig('traces.pdf', format="pdf",
            bbox_inches='tight', pad_inches=0.05)
plt.show()