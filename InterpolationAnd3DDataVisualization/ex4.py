import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import RectBivariateSpline

data = np.load("inter2D.npz")
x = data["x"]
y = data["y"]
z = data["z"]

X, Y = np.meshgrid(x, y)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(X, Y, z, rstride=3, cstride=3)
plt.show()

spline = RectBivariateSpline(x, y, z)

xx = np.linspace(0, 10, 200)
yy = np.linspace(0, 10, 200)
XX, YY = np.meshgrid(xx, yy)
ZZ = spline(xx, yy)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(XX, YY, ZZ, cmap='jet')
plt.show()
