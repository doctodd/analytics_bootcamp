"""
Gets N samples from exponential distribution of random numbers, then plot the mean of those samples. Repeat TRIALS times
Should produce a normal curve that skews left a bit because of the exp function
"""

from stats import *
import time
import matplotlib.pyplot as plt


setseed( int( round(time.time() * 1000)) )  # Set seed based on current time in milliseconds
N = 100  # number of samples taken from the random distribution which we later average
TRIALS = 4000 # number of times we take N samples and average them
LAMBDUH = 1.5
X_=[]

# Plot the experimental data pulled from exponential distribution
for i in range (TRIALS):
    X = [rexp(LAMBDUH) for t in range(N)]
    X_.append(math.fsum(X)/N)

fig = plt.figure()
ax = fig.add_subplot(111)

plt.hist(X_, bins=40, normed=1)

# Plot the theoretical normal distribution
sigma = math.sqrt(1/LAMBDUH**2/N)
mu = LAMBDUH ** -1
x = np.arange(min(X_), max(X_), 0.01)

y = normpdf(x, mu, sigma)
plt.plot(x, y)

plt.text(.02,.9, '$N = %d$' % N, transform = ax.transAxes)
plt.text(.02, .85, '$TRIALS = %d$' % TRIALS, transform = ax.transAxes)
plt.text(.02, .8, 'mean($\\overline{X}$) = %f' % np.mean(X_), transform = ax.transAxes)
plt.text(.02, .75, 'var($\\overline{X}$) = %f' % np.var(X_), transform = ax.transAxes)
plt.text(.02, .7, 'mean Exp($%f$) = %f' % (LAMBDUH, 1/LAMBDUH), transform = ax.transAxes)
plt.text(.02, .65, 'var Exp($%f$/%d = %f' % (LAMBDUH, N, (1/LAMBDUH**2/N)), transform = ax.transAxes)

plt.title("CLT Density Demo. sample mean of Exp($\lambda=1.5$) is $N(1/\lambda, (1/\lambda^2)/N)$")
plt.xlabel("$\\overline{X}$", fontsize=16)
plt.ylabel("Density", fontsize=16)
plt.axis([0,1.333,0,5])

plt.savefig('clt_exp-' + str(TRIALS) + '-' + str(N) + '.pdf', format="pdf")

plt.show()