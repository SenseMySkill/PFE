import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, CubicSpline

data = np.load("inter1D.npz")
x = data["x"]
y = data["y"]

lin = interp1d(x, y, kind='linear')
quad = interp1d(x, y, kind='quadratic')

cubic = CubicSpline(x, y)

xx = np.linspace(-1.0, 1.0, 500)

plt.scatter(x, y, label="points")
plt.plot(xx, lin(xx), label="linear")
plt.plot(xx, quad(xx), label="quadratic")
plt.plot(xx, cubic(xx), label="cubic spline")
plt.legend()
plt.show()
