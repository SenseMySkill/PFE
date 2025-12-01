import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import cm

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

def simulate(k):
    u = np.exp(-0.5 * ((x - x0) / sigma)**2)
    U_hist = [u.copy()]
    T_hist = [0.0]
    mass = [np.trapz(u, x)]
    t = 0.0
    while t < T_final:
        u_new = u.copy()
        u_new[1:-1] = u[1:-1] + r*(u[:-2] - 2*u[1:-1] + u[2:]) - k*dt*u[1:-1]
        u_new[0] = u[0] + r*(u[1] - u[0]) - k*dt*u[0]
        u_new[-1] = u[-1] + r*(u[-2] - u[-1]) - k*dt*u[-1]
        u = u_new
        t += dt
        U_hist.append(u.copy())
        T_hist.append(t)
        mass.append(np.trapz(u, x))
    return np.array(U_hist), np.array(T_hist), np.array(mass)

U0, T0, M0 = simulate(0)
U1, T1, M1 = simulate(1)

fig, ax = plt.subplots()
im = ax.imshow(U0.T, aspect='auto', origin='lower',
               extent=[0, T_final, 0, L])
plt.colorbar(im)
ax.set_title("Heatmap u(x,t), k = 0")
ax.set_xlabel("t")
ax.set_ylabel("x")
plt.show()

fig, ax = plt.subplots()
im = ax.imshow(U1.T, aspect='auto', origin='lower',
               extent=[0, T_final, 0, L])
plt.colorbar(im)
ax.set_title("Heatmap u(x,t), k = 1")
ax.set_xlabel("t")
ax.set_ylabel("x")
plt.show()

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.set_xlim(0, L)
ax.set_ylim(0, U0.max())
ax.set_title("Animated profile (k = 0)")
def init():
    line.set_data([], [])
    return (line,)
def update(frame):
    line.set_data(x, U0[frame])
    line.set_color(cm.plasma(frame/len(U0)))
    return (line,)
anim = FuncAnimation(fig, update, frames=len(U0), init_func=init, interval=20, blit=True)
plt.show()

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.set_xlim(0, L)
ax.set_ylim(0, U1.max())
ax.set_title("Animated profile (k = 1)")
def update2(frame):
    line.set_data(x, U1[frame])
    line.set_color(cm.plasma(frame/len(U1)))
    return (line,)
anim = FuncAnimation(fig, update2, frames=len(U1), init_func=init, interval=20, blit=True)
plt.show()

plt.plot(T0, M0, label="k = 0")
plt.plot(T1, M1, label="k = 1")
plt.xlabel("Time t")
plt.ylabel("Total mass ∫u dx")
plt.title("Total mass over time: k = 0 vs k = 1")
plt.legend()
plt.show()
