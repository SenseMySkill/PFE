import numpy as np
import matplotlib.pyplot as plt

x = np.load("daneX.npy")
y = np.load("daneY.npy")

hist, xedges, yedges = np.histogram2d(x, y, bins=50)

plt.imshow(hist.T, origin='lower',
           extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]],
           aspect='auto', cmap='jet')
plt.colorbar()
plt.show()

X, Y = np.meshgrid(xedges, yedges)
plt.contourf(X[:-1, :-1], Y[:-1, :-1], hist.T, cmap='jet')
plt.colorbar()
plt.show()
