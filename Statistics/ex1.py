import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

#==========1==========
print("\n==========1==========\n")

samples = np.random.normal(3.0, 1.0, 100)

print(samples)

plt.hist(samples, bins=10, alpha=0.5)

#==========2==========
print("\n==========2==========\n")

samples2 = np.random.normal(1.0, 2.0, 100)

print(samples2)

plt.hist(samples2, bins=10, alpha=0.5)

plt.show()

#==========3==========
print("\n==========3==========\n")

mean1 = np.mean(samples)
mean2 = np.mean(samples2)
thresh = 0.5 * (mean1+mean2)

samples_below = sum(samples < thresh)
samples2_below = sum(samples2 >= thresh)

samples_overlap = samples_below / len(samples)
samples2_overlap = samples2_below / len(samples2)

misclass = (samples_overlap + samples2_overlap) / 2

print(misclass)

#==========4==========
print("\n==========4==========\n")

mu_hat = np.mean(samples)
sigma_hat = np.std(samples, ddof=1)
print(mu_hat, sigma_hat)

#==========5==========
print("\n==========5==========\n")

samples3 = []
means3 = []
for i in range(100):
    sample = np.random.normal(3.0,1.0,100)
    mean = np.mean(sample)
    samples3.append(sample)
    means3.append(mean)

plt.hist(means3, bins=10)
plt.show()

means3 = np.array(means3)
se = np.std(means3, ddof=1)

print(se)

#==========6==========
print("\n==========6==========\n")

means4 = []
for i in range(1000):
    sample = np.random.normal(3.0, 1.0, 100)
    mean = np.mean(sample)
    means4.append(mean)

means4 = np.array(means4)
se_1000 = np.std(means4, ddof=1)

print("SE dla 100 próbek:", se)
print("SE dla 1000 próbek:", se_1000)