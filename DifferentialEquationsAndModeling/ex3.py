import numpy as np
import matplotlib.pyplot as plt

r = 20
K = 1_000_000
N0 = 1
target = 500_000

t = np.linspace(0, 1, 1000000)
N = K / (1 + ((K - N0) / N0) * np.exp(-r * t))

idx = np.argmin(np.abs(N - target))
t_target = t[idx]
print(t_target)

plt.plot(t, N)
plt.yscale('log')
plt.xlabel("Time (hours)")
plt.ylabel("Bacteria count")
plt.title("Logistic growth of bacteria")
plt.grid(True, which="both", ls="--")
plt.show()
