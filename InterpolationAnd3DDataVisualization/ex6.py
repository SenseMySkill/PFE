import numpy as np
import matplotlib.pyplot as plt

data = np.load("dataBar3D.npy")

x = np.arange(data.shape[1])

plt.bar(x, data[0], label='A')
plt.bar(x, data[1], bottom=data[0], label='B')
plt.bar(x, data[2], bottom=data[0] + data[1], label='C')

plt.legend()
plt.show()
