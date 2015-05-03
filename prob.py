import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import collections
x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]
c= collections.Counter(x)
print c
count_sum = sum(c.values())
for k,v in c.iteritems():
print "The frequency of " + str(k) + "is " + str(float(v) / count_sum)
plt.boxplot(x)
plt.show()
plt.hist(x, histtype='bar')
plt.show()
plt.figure()
test_data = np.random.normal(size=1000)
graph1 = stats.probplot(test_data, dist="norm", plot=plt)
plt.show()
plt.figure()
test_data2 = np.random.uniform(size=1000)
graph2 = stats.probplot(test_data2, dist="norm", plot=plt)
plt.show()

