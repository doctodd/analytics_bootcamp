"""
Hypothesis testing lab (is free beer good for tips?)
"""

from stats import *
import matplotlib.pyplot as plt
import math
import numpy as np
from scipy.stats import t

# the data
tips = [20.8, 18.7, 19.1, 20.6, 21.9, 20.4, 22.8, 21.9, 21.2, 20.3, 21.9, 18.3, 21.0, 20.3, 19.2,
        20.2, 21.1, 22.1, 21.0, 21.7]

# useful numbers
N = len(tips)
mean =  math.fsum(tips)/N
sampvar = var(tips)

# prep for figure annotating
fig = plt.figure()
ax = fig.add_subplot(111)

# plot data as simple histogram
plt.hist(tips, bins=5, normed=1)

# annotate graph
plt.title("Sample Tips After Free Beer")
plt.xlabel("Tip %", fontsize=16)
plt.ylabel("Density", fontsize=16)
plt.text(.02, .5, "Sample mean = %f" % mean, transform = ax.transAxes)
plt.show()

# next show where the mean falls on the normal curve of means centered on 20%
stddev = math.sqrt(abs(sampvar)/N)  # we don't know the actual variance, so we assume same as sample variance
mean_norm = 20.0
x = np.arange(18.0, 22.0, 0.001)

# y = normpdf(x, mu, sigma)  # was used in step 5 replaced with...
y = normpdf(x, mean_norm, stddev)
plt.axis([18.0, 22.0, 0, 1.6])
plt.plot(x, y, color = "red")
plt.title("Tips control (H0) sample mean density N(%d,s^2/n)" % N)
plt.xlabel("Average Tip %", fontsize=16)
plt.ylabel("Density", fontsize=16)
plt.plot(mean, 0, "bD")
plt.text(0.65, .05, "Sample mean = %f" % mean, transform = ax.transAxes)
plt.show()

# t-test
ttest = (mean-mean_norm)/(np.std(tips, ddof=1)/math.sqrt(N))
print "t value = %f" % ttest

# p-value
p = t.sf(ttest,N-1)
print "p value = %f" % (2*p)

# bootstrapping for empirical hypothesis testing (estimate a p-value)
TRIALS = 5000
X_ = []

for i in range (TRIALS):  # collect TRIALS number of bootstrap samples
    X = [rnorm(N, mean_norm, sampvar) for t in range(N)]  # each bootstrap sample is size len(tips)
    X_.append(math.fsum(X)/len(X))  # for each bootstrap sample, find the mean, and put it in a new list

greater = sum([x >= np.mean(tips) for x in X_])  # counts up how many means in X_ are >= the sample mean
print greater
pboot = 2 * greater/float(TRIALS)
print pboot
print "Bootstraped p value estimate = %f" % pboot

# write out results in text file
text_file = open("hyp_results.txt", "w")
text_file.write("t value = %f\n" % ttest)
text_file.write("p value = %f\n" % (2*p))
text_file.write("Bootstraped p value estimate = %f\n" % pboot)
text_file.close()