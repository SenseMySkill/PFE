import numpy as np
import matplotlib.pyplot as plt

data = np.load("dataBar3D.npy")
sample = data[0]

n = len(sample)
x = np.tile(np.arange(n), n)
y = np.repeat(np.arange(n), n)
z = np.zeros(n*n)

dx = np.ones(n*n)
dy = np.ones(n*n)
dz = sample[y]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

colors = plt.cm.jet(y / y.max())

ax.bar3d(x, y, z, dx, dy, dz, color=colors, zsort='average')

plt.show()
