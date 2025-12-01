import numpy as np
import matplotlib.pyplot as plt

r = 0.5
K = 10

t = np.linspace(0, 10, 20)
N = np.linspace(0, 12, 20)
T, NN = np.meshgrid(t, N)

dN_exp = r * NN
dT = np.ones_like(dN_exp)

plt.figure(figsize=(6,5))
plt.quiver(T, NN, dT, dN_exp)
plt.streamplot(T, NN, dT, dN_exp, color=dN_exp, cmap='viridis')
plt.title("Exponential Growth")
plt.xlabel("Time")
plt.ylabel("Population Size N")
plt.tight_layout()
plt.show()

dN_log = r * NN * (1 - NN / K)

plt.figure(figsize=(6,5))
plt.quiver(T, NN, dT, dN_log)
plt.streamplot(T, NN, dT, dN_log, color=dN_log, cmap='plasma')
plt.title("Logistic Growth")
plt.xlabel("Time")
plt.ylabel("Population Size N")
plt.tight_layout()
plt.show()
