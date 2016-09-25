from stats import *
import time
import matplotlib.pyplot as plt
import numpy as np

setseed( int( round(time.time() * 1000)) )  # Set seed based on current time in milliseconds


prices = []
f = open("prices.txt")
for line in f:
    v = float(line.strip())
    prices.append(v)

TRIALS = 500
X_ = []

fig = plt.figure()
ax = fig.add_subplot(111)

for i in range (TRIALS):
    X_.append(math.fsum(sample(prices))/len(prices))

X_.sort()
inside = [X_[i] for i in range(int(TRIALS*0.025), int(TRIALS*0.975))]
plt.plot([inside[0], inside[-1]], [0,0], "bD")  # upper and lower ranges of the 95% confidence interval

mu = np.mean(prices)
stddev = math.sqrt(abs(var(X_)))  # we don't know the actual variance, so we assume same as sample variance

x = np.arange(1.05, 1.25, 0.001)
y = normpdf(x, mu, stddev)
plt.plot(x, y, color = "red")  # theoretical normal distribution

left = mu - 1.96*stddev
right = mu + -1.96*stddev

ci_x = np.arange(left, right, 0.001)
ci_y = normpdf(ci_x, mu, stddev)
# shade under the ci_x, ci_y curve
plt.fill_between(ci_x, ci_y, color = "#F8ECE0")

plt.axis([1.10, 1.201, 0, 30])
plt.text(.02,.95, '$TRIALS = %d$' % TRIALS, transform = ax.transAxes)
plt.text(.02,.9, '$mean(prices)$ = %f' % np.mean(prices), transform = ax.transAxes)
plt.text(.02,.85, '$mean(\\overline{X})$ = %f' % np.mean(X_), transform = ax.transAxes)
plt.text(.02,.80, '$stddev(\\overline{X})$ = %f' % np.std(X_,ddof=1), transform = ax.transAxes)
plt.text(.02,.75, '95%% CI = $%1.2f \\pm 1.96*%1.3f$' % (np.mean(X_),np.std(X_,ddof=1)), transform = ax.transAxes)
plt.text(.02,.70, '95%% CI = ($%1.2f,\\ %1.2f$)' % (np.mean(X_)-1.96*np.std(X_), np.mean(X_)+1.96*np.std(X_)),
         transform = ax.transAxes)

plt.text(1.135, 11.5, "Expected", fontsize=16)
plt.text(1.135, 10, "95% CI $\\mu \\pm 1.96\\sigma$", fontsize=16)
plt.title("95% Confidence Intervals: $\\mu \\pm 1.96\\sigma$", fontsize=16)

ax.annotate("Empirical 95% CI",
             xy=(inside[0], .3),
             xycoords="data",
             xytext=(1.13,4), textcoords='data',
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3"),
             fontsize=16)
plt.savefig('conf-%d.pdf' % TRIALS, format="pdf")

plt.show()