import numpy as np
import matplotlib.pyplot as plt

L = 1.0
nx = 101
dx = L/(nx-1)
x = np.linspace(0, L, nx)

D = 0.01
dt = 0.0001
tmax = 2.0
nt = int(tmax/dt)

u = np.zeros(nx)
u[int(nx*0.1):int(nx*0.2)] = 1.0

mass_history = []
time = []

for n in range(nt):
    un = u.copy()
    u[1:-1] = un[1:-1] + D*dt/dx**2*(un[2:] - 2*un[1:-1] + un[:-2])
    u[0] = u[1]
    u[-1] = u[-2]
    mass_history.append(np.trapz(u, x))
    time.append(n*dt)

plt.plot(time, mass_history)
plt.xlabel("czas")
plt.ylabel("masa całkowita")
plt.title("Total mass over time (k = 0)")
plt.show()
