import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm  # do colormap

data = np.load("dataBar3D.npy")
sample = data[0]

n = len(sample)

x = np.tile(np.arange(n), n)
y = np.repeat(np.arange(n), n)
z = np.zeros(n*n)

dx = np.ones(n*n)
dy = np.ones(n*n)
dz = sample[y]

norm = plt.Normalize(dz.min(), dz.max())
colors = cm.jet(norm(dz))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.bar3d(x, y, z, dx, dy, dz, color=colors, alpha=0.8, zsort='average')

plt.show()
