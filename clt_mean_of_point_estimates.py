'''
Central Limit Theorem for mean of point estimates:
Stdev of sampling distribution == Std Error
where Std Error = Stdev of population distribution / root of sample size
since population distribution is unknown,
its Stdev is approximated by any chosen sample.
'''

'''
We want to verify the equation above by setting simulation:
* Generate a sample of points in size of "n_sample"
* Compute the mean of points in that sample
* Repeat the steps above for "n_xbar" times to collect sampling of means
* Compute Stdev of means aka sampling distribution
* Compute Std Error as Stdev of last simulated sample divided by root of "n_sample"
* Verify that the Std Error approximates the Stdev of sampling distribution
* Visualize the distribution of means aka sampling distribution
'''

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

mu, sigma = 0., 1.  # true population parameters for simulation

n_sample = 50  # number of proportions aka sample size
n_xbar = 1000  # number of means of proportions aka sampling size

xbar = []
for _ in range(n_xbar):
	x = np.random.normal(loc=mu, scale=sigma, size=n_sample)
	xbar.append(x.mean())

xbar = np.array(xbar)

stdev_xbar = np.sqrt(((xbar - xbar.mean())**2).mean())

SE = np.sqrt(((x - x.mean())**2).mean() / n_sample)

print(f"\nSet mu =\t{mu}")
print(f"Set sigma =\t{sigma}")
print(f"Stdev xbar =\t{stdev_xbar}")
print(f"Std Error =\t{SE}")

sns.histplot(xbar, binwidth=stdev_xbar/5, kde=True)
plt.show()
