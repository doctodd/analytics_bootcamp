import matplotlib.pyplot as plt
import numpy as np

N = 1000
X = [np.random.uniform(2, 8) for i in range(N)]

plt.hist(X, normed=1)

plt.title("U(2,8) Density Demo")
plt.xlabel("X", fontsize=16)
plt.ylabel("Density", fontsize=16)
plt.axis([2, 8, 0, .25])

#fig = plt.figure()
#ax = fig.add_subplot(111)
# put N=... at top left
#plt.text(.1,.9, 'N = %d' % N, fontsize=16, transform = ax.transAxes)
plt.text(2.1,.23, 'N = %d' % N, fontsize=16)

plt.savefig('unif-2-8-density-fancy.pdf', format='pdf')
plt.show()
