"""
Generate random normal variables using the Central Limit Theorem
"""

from stats import *
import time
import matplotlib.pyplot as plt

setseed( int( round(time.time() * 1000)) )  # Set seed based on current time in milliseconds

N = 100
TRIALS = 4000
mean = 2
variance = 2
# X = [rnorm01(N) for t in range(TRIALS)]  # was used in Step 3 of exercise. Replaced with...

X = [rnorm(N, mean, variance) for t in range(TRIALS)]

#fig = plt.figure()
#ax = fig.add_subplot(111)

plt.axis([-4, 7, 0, 0.5])
plt.hist(X, bins=40, normed=1)

# Plot real normal curve, variance = 1 and centered around 0 (i.e. mu = 0)
sigma = 1
mu = 0
x = np.arange(min(X), max(X), 0.01)

# y = normpdf(x, mu, sigma)  # was used in step 5 replaced with...
y = normpdf(x, mean, math.sqrt(abs(variance)))
plt.plot(x, y, color = "red")

plt.savefig('rnorm-%d-%d-%d-%d.pdf' % (mean, variance, TRIALS, N), format="pdf")
plt.show()