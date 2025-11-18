import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(0, 3*np.pi)
y1 = np.sin(x1)

x2 = np.linspace(0, 3*np.pi)
y2 = np.cos(x2)

diff = np.abs(y1-y2)
mask = diff < 0.1

plt.plot(x1,y1)
plt.plot(x2,y2)
plt.scatter(x1[mask], y1[mask], color='red')

plt.show()

print(np.where(mask))