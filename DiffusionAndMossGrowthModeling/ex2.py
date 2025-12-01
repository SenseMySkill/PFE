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
u = np.exp(-0.5 * ((x - x0) / sigma)**2)
U_hist = [u.copy()]
T_hist = [0.0]
t = 0.0

while t < T_final:
    u_new = u.copy()
    u_new[1:-1] = u[1:-1] + r * (u[0:-2] - 2*u[1:-1] + u[2:])
    u_new[0] = u[0] + r * (u[1] - u[0])
    u_new[-1] = u[-1] + r * (u[-2] - u[-1])
    u = u_new
    t += dt
    U_hist.append(u.copy())
    T_hist.append(t)

U_hist = np.array(U_hist)
T_hist = np.array(T_hist)

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.set_xlim(0, L)
ax.set_ylim(0, U_hist.max())
ax.set_xlabel("x")
ax.set_ylabel("u(x,t)")
ax.set_title("Animated diffusion profile")
cmap = cm.plasma

def init():
    line.set_data([], [])
    return (line,)

def update(frame):
    line.set_data(x, U_hist[frame])
    line.set_color(cmap(frame / len(U_hist)))
    return (line,)

anim = FuncAnimation(fig, update, frames=len(U_hist), init_func=init, interval=30, blit=True)
plt.show()
