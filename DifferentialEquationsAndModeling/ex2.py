import numpy as np
import matplotlib.pyplot as plt

N0 = 10
N240 = 1015
t_obs = 240
t_target = 20 * 24

r = (1 / t_obs) * np.log(N240 / N0)
N_target = N0 * np.exp(r * t_target)

t = np.linspace(0, t_target, 400)
N_t = N0 * np.exp(r * t)

print(N_target)

plt.figure(figsize=(8,5))
plt.plot(t, N_t)
plt.yscale('log')
plt.xlabel("Time (hours)")
plt.ylabel("Number of plants")
plt.title("Exponential growth of Wolffia microscopica")
plt.grid(True, which="both", ls="--")
plt.show()
