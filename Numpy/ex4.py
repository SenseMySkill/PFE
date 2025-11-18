import numpy as np
import matplotlib.pyplot as plt

x = np.random.uniform(-1,1, 500)
y = np.random.uniform(-1,1, 500)

r = np.sqrt(x**2 + y**2)
t = np.arctan2(y,x)
t = (t + 2*np.pi) % 2*np.pi

maskj = t < np.pi
maskt = t >= np.pi

fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')

plt.scatter(t[maskj], r[maskj], c=t[maskj], cmap='jet')
plt.scatter(t[maskt], r[maskt], c=t[maskt], cmap='jet')

plt.show()