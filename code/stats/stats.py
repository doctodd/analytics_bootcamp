__author__ = 'Todd'

import numpy as np
import random
import math
import time


def mean(x):  # Return the mean value of a list of integers
    sum = 0
    for value in x:
        sum = sum + value
    return sum/len(x)


def var(x):  # Return the variance of a list of integers
    m = mean(x)
    N = float(len(x))  # Make N a float, so the division works later
    sum = 0
    for value in x:
        sum += (value - m)**2
    return (1/(N-1))*sum


def cov(x,y):  # Return the covariance of 2 lists of integers (or 0 if they differ in length)
    mx = mean(x)
    my = mean(y)
    N = float(len(x))
    sum = 0
    if len(x) == len(y):
        for i in xrange(0, len(x)):
            sum += (x[i]-mx)*(y[i]-my)
        return (1/(N-1))*sum
    else:
        return 0


a = 16807
m = pow(2,31)-1
x = 666 # this is our x_n that changes each runif01() call

def runif01(): # U(0,1)
    global x
    x = a * x % m
    return x / float(m)

def setseed(s): # updates the seed global variable
    global x
    x = s

def runif(a,b):
    rv = runif01()
    return a + (b-a)*rv

def rbinomial(n,p):  # Sim with probability p, N Bernoulli trials, return successes
    success = 0
    for i in range(0,n):
        test = runif01()
        if test <= p:
            success += 1
    return success

def rexp(lambduh):  # Returns a random value from the exponential distribution using the inverse transform method
    u = runif01()
    return -1*math.log(1-u)/lambduh

def exppdf(x, lambduh):  # Returns the exponential probability distribution function
    return lambduh*math.exp(-1*lambduh*x)

def unifvar(a, b):
    return ((b-a)**2)/float(12)

def normpdf(x, mu, sigma):  # value, mean, standard deviation = sqrt(variance), so be sure to pass the correct value
    coeff = 1.0/(abs(sigma) * math.sqrt(2*math.pi))
    power = - (x - mu)**2 / (abs(sigma)**2 * 2.0)
    result = coeff*math.e ** power
    return result

def rnorm01(N):  # return a value from N(0,1)
    X = [runif01() for t in range(N)]
    X_ = math.fsum(X) / N
    rv = X_ - 0.5
    Z = rv/math.sqrt(var(X)/N)
    return Z

def rnorm(N, mean, variance):
    sigma = math.sqrt(abs(variance))
    Z = rnorm01(N)

    X = mean + Z*sigma
    return X

def sample(data):
    """
    Return a random sample of data values with replacement.
    The returned array has the same length as data.
    """
    i = [int(runif(0,len(data))) for t in range (len(data))]  # generate a list of random indices
    return [data[j] for j in i]  # return a list of the data values that go with those indices
