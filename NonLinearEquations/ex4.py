import numpy as np
import matplotlib.pyplot as plt

data = np.random.rand(10, 2) * 10

inc = np.arange(10)

datashift1 = data + inc[:, np.newaxis]

datashift2 = datashift1.copy()
datashift2[:, 0] += 3

datashift3 = datashift2.copy()
theta = np.pi / 4
R = np.array([[np.cos(theta), -np.sin(theta)],
              [np.sin(theta), np.cos(theta)]])
datashift3 = datashift3 @ R.T

x = datashift3[:, 0]
y = datashift3[:, 1]

A = np.column_stack((np.ones_like(x), x))

w, residuals, rank, s = np.linalg.lstsq(A, y, rcond=None)

x_line = np.linspace(min(x), max(x), 200)
y_line = w[0] + w[1] * x_line

plt.scatter(x, y, label="Transformed data points")
plt.plot(x_line, y_line, color="red", label="Least squares line")

plt.show()

print(w)