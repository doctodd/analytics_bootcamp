"""
Gets N samples from uniform distribution of random numbers, then plot the mean of those samples. Repeat TRIALS times
Should produce a normal curve
"""

from stats import *
import time
import matplotlib.pyplot as plt


setseed( int( round(time.time() * 1000)) )  # Set seed based on current time in milliseconds
N = 20  # number of samples taken from the random distribution which we later average
TRIALS = 2000 # number of times we take N samples and average them
X_=[]

for i in range (TRIALS):
    X = [runif01() for t in range(N)]
    Xsum = math.fsum(X)
    X_.append(Xsum/N)

fig = plt.figure()
ax = fig.add_subplot(111)

plt.hist(X_, bins=60, normed=1)

b = 1.0  # max value of the range
a = 0  # min value of the range

sigma = math.sqrt(unifvar(a, b)/N)
mu = (a + b)/2.0
x = np.arange(min(X_), max(X_), 0.01)

y = normpdf(x, mu, sigma)
plt.plot(x, y, color="red")

plt.text(.02,.9, '$N = %d$' % N, transform = ax.transAxes)
plt.text(.02, .85, '$TRIALS = %d$' % TRIALS, transform = ax.transAxes)
plt.text(.02, .8, 'mean($\\overline{X}$) = %f' % np.mean(X_), transform = ax.transAxes)
plt.text(.02, .75, 'var($\\overline{X}$) = %f' % np.var(X_), transform = ax.transAxes)
plt.text(.02, .7, 'var U($0,1$)/%d = %f' % (N, unifvar(0,1)/N), transform = ax.transAxes)

plt.title("CLT Density Demo. sample mean of U(0,1) is $N(.5, \sigma^2/N)$")
plt.xlabel("$\\overline{X}$", fontsize=16)
plt.ylabel("Density", fontsize=16)

plt.savefig('clt_unif-' + str(TRIALS) + '-' + str(N) + '-fancier.pdf', format="pdf",
            bbox_inches='tight', pad_inches=0.05)

plt.show()