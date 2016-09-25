from stats import *
import time
import matplotlib.pyplot as plt
import scipy.misc as misc

def binom(n, k, p):
    return misc.comb(n, k)*pow(p,k)*pow((1-p),(n-k))

setseed( int( round(time.time() * 1000)) )  # Set seed based on current time in milliseconds
n = 500
p = 0.4
SAMPLES = 5000

X = [rbinomial(n,p) for t in range(SAMPLES)]
Y = [binom(n, k, p) for k in range(0,n+1,5)]

plt.hist(X, normed=1)
plt.bar(range(0,n+1,5), Y, color='red', align='center', width=1)
plt.axis([150,250,0,.05])  # set the axes so that we get a close-up
plt.text(160,0.04, '$n = %d$' % n, fontsize=16)
plt.text(160,0.037, '$p = %f$' % p, fontsize=16)
plt.text(160,0.034, '$SAMPLES = %d$' % SAMPLES, fontsize=16)

plt.show()