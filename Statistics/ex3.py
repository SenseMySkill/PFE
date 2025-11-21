import numpy as np
import matplotlib.pyplot as plt

data_flat = np.genfromtxt("PCAdata.txt", skip_header=0)  # skip_header=1 jeśli jest nagłówek
data = data_flat.reshape(-1, 3)

print(data.shape)

means = np.mean(data, axis=0)
print(means)

cov_matrix = np.cov(data, rowvar=False)
print(cov_matrix)

corr_matrix = np.corrcoef(data, rowvar=False)
print(corr_matrix)

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

x = data[:, 0]
y = data[:, 1]
z = data[:, 2]

ax.scatter(x, y, z, c='green', marker='o', s=60)

plt.show()
