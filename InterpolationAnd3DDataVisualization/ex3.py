import numpy as np
import matplotlib.pyplot as plt

x = np.load("daneX.npy")
y = np.load("daneY.npy")

hist, xedges, yedges = np.histogram2d(x, y, bins=100)

X, Y = np.linspace(0, 100, 100), np.linspace(0, 100, 100)
X, Y = np.meshgrid(X, Y)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, hist.T, cmap='jet')
plt.show()
