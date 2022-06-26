'''
Central Limit Theorem for proportion:
Stdev of sampling distribution == Std Error
where Std Error = Stdev of population distribution / root of sample size
since population distribution is unknown,
its Stdev is approximated by any chosen sample.
'''

'''
We want to verify the equation above by setting simulation:
* Roll a 100-sided die for "n_sample" times
* Count the number of times aka "cnt_success" when rolled outcome is no greater than the percentage of true successful probability
* Record the proportion of success in this sample as "p_hat"
* Repeat the steps above for "n_prop" times to collect sampling of proportions
* Compute Stdev of proportions aka sampling distribution
* Compute Std Error as Stdev of last simulated sample divided by root of "n_sample"
* Verify that the Std Error approximates the Stdev of sampling distribution
* Visualize the distribution of proportions aka sampling distribution
'''

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def simulate(p_true=.5):

	p_hat = []
	for _ in range(n_prop):
		cnt_success = 0
		for _ in range(n_sample):
			cnt_success += int(np.random.choice(range(100)) < (p_true*100))
		p_hat.append(cnt_success/n_sample)
	p_hat = np.array(p_hat)

	stdev_prop = np.sqrt(((p_hat - p_hat.mean())**2).mean())
	SE = np.sqrt(p_hat[-1] * (1-p_hat[-1]) / n_sample)

	print(f"\nSet p_true =\t{p_true}")
	print(f"Stdev Props =\t{stdev_prop}")
	print(f"Std Error =\t{SE}")

	sns.histplot(p_hat, binwidth=stdev_prop/5)

	return None


'''
Choose a list of true successful probabilities for die-roll simulation
Notice that:
* The closer "p_true" to 0% or 100%, the more skewed and less variable
* The closer "p_true" to 50%, the more centred and more variable
* Intuitively speaking, 50-50 blind guess implies absolute uncertainty
'''
p_true_choices = [.05, .5, .95]

n_sample = 100  # number of times rolling a die aka sample size
n_prop = 1000  # number of proportions aka sampling size

for p_true in p_true_choices:
	simulate(p_true=p_true)

plt.xlim(0,1)
plt.ylim(0,n_prop/5)
plt.show()
