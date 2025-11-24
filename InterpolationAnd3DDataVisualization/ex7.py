import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

data = np.load("dataBar3D.npy")
sample = data[0]

x = np.arange(len(sample))
y = np.zeros(len(sample))
z = np.zeros(len(sample))

dx = np.ones(len(sample))
dy = np.ones(len(sample))
dz = sample

norm = plt.Normalize(dz.min(), dz.max())
colors = cm.jet(norm(dz))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.bar3d(x, y, z, dx, dy, dz, color=colors, alpha=0.8, zsort='average')

plt.show()
