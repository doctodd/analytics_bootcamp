from stats import *
import matplotlib.pyplot as plt
import time
import numpy as np

setseed( int( round(time.time() * 1000)) )  # Set seed based on current time in milliseconds

N = 4000
LAMBDUH = 1.5

y = [rexp(LAMBDUH) for t in range(N)]
plt.hist(y, bins = 40, normed=1)

x = np.arange(0, 6, 0.01)
y = [exppdf(v, LAMBDUH) for v in x]

plt.plot(x,y, color = "red")
plt.show()
