import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(-1, 10, 200)

x2_line1 = (4 - 2*x1) / 3
x2_line2 = (23 - 5*x1) / 4
x2_line3 = 18 / 5 * np.ones_like(x1)

plt.plot(x1, x2_line1)
plt.plot(x1, x2_line2)
plt.plot(x1, x2_line3)

A = np.array([[2, 3],
              [5, 4]])
b = np.array([4, 23])
x = np.linalg.solve(A, b)

plt.scatter(x[0], x[1])

plt.show()