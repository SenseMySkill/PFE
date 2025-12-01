import numpy as np
import matplotlib.pyplot as plt

L = 1.0
N = 300
D = 0.1
T_final = 2.0
x = np.linspace(0, L, N+1)
dx = x[1] - x[0]
dt = 0.5 * dx**2 / D
r = D * dt / dx**2
x0 = 0.3
sigma = 0.03
u = np.exp(-0.5 * ((x - x0) / sigma)**2)
U_hist = [u.copy()]
t = 0.0

while t < T_final:
    u_new = u.copy()
    u_new[1:-1] = u[1:-1] + r * (u[0:-2] - 2*u[1:-1] + u[2:])
    u_new[0] = u[0] + r * (u[1] - u[0])
    u_new[-1] = u[-1] + r * (u[-2] - u[-1])
    u = u_new
    U_hist.append(u.copy())
    t += dt

U_hist = np.array(U_hist)
plt.imshow(U_hist, origin='lower', aspect='auto', extent=[0, L, 0, T_final])
plt.xlabel('x')
plt.ylabel('t')
plt.colorbar(label='stężenie')
plt.show()
