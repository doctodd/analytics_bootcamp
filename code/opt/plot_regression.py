from pylab import show, text, imshow, plot
import matplotlib.pyplot as plt
import random, time
from minimize import *

# NOTE: analytic solution is (-36.000625, 15.484375)

# Average hourly wage
HOURLY_WAGE = [2.98, 3.09, 3.23, 3.33, 3.46, 3.6, 3.73, 2.91, 4.25, 4.47, 5.04, 5.47, 5.76]
# Number of homicides per 100,000 people
MURDERS = [8.6, 8.9, 8.52, 8.89, 13.07, 14.57, 21.36, 28.03, 31.49, 37.39, 46.26, 47.24, 52.33]

# Variables
LEARNING_RATE = (500,100) # Eta
h = 0.000001  # Step size
PRECISION = 0.000001

def Cost(B,X=HOURLY_WAGE,Y=MURDERS):
	cost = 0.0
	for i in xrange(0,len(X)):
		cost += (B[0] + B[1]*X[i] - Y[i])**2
	return cost


def heatmap(f, trace=None): # trace is a list of [b1, b2] pairs
	b1 = [i for i in xrange(-60,-14)]  #  The x axis of the heat map (intercept)
	b2 = [i for i in xrange(5,26)]  # The y axis of the heat map (slope)
	C = [[0 for i in b2] for j in b1]  # Initialize the Cost matrix
	i = 0
	j = 0
	for m in b1:  # Calculate the cost at each x,y
		for n in b2:
			pos = (m,n)
			C[i][j] = (f(pos))
			j += 1
		i += 1
		j = 0

	# Plot the heat map
	vmax = np.abs(C).max()
	vmin = -np.abs(C).max()
	imshow(C,
		origin='lower',
		   extent=[min(b1), max(b1), min(b2), max(b2)],
		   vmax=np.abs(C).max(), vmin=-np.abs(C).max()
	)

	# Plot the start, stop, and trace.
	p0 = []
	p1 = []
	# fill in trace[0:]
	for pair in trace:
		p0.append(pair[0])
		p1.append(pair[1])

	plot(p0, p1, "ko", markersize=1)
	plt.title('Trace in heat map')
	plt.xlabel('b1', style='italic')
	plt.ylabel('b2', style='italic')
	start = trace[0]
	stop = trace[-1]
	plot(start[0], start[1], 'ro', markersize=5)
	plot(stop[0], stop[1], 'ro', markersize=5)
	plt.text(start[0], start[1]+ .5,'start')
	plt.text(stop[0], stop[1]+ .5,'stop')
	plt.text(-55, 23, 'steps=%r' % len(trace))
	return


# Randomly select a starting point, B0
random.seed(int(round(time.time() * 1000)))
B0 = (random.randrange(-55,-19,1), random.randrange(10,21,1))
#B0 = (random.randrange(5,26,1), random.randrange(-60,-14,1))

# Minimize the cost function and get the start and end times
begin = time.time()
(m,steps,trace) = minimize(Cost, B0, LEARNING_RATE, h, PRECISION)
end = time.time()


heatmap(Cost, trace)

show()
