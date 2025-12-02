import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#Parametry symulacji
Nx, Ny = 200, 200     # rozmiar siatki
dx = dy = 1.0         # krok przestrzenny
D = 0.5               # współczynnik dyfuzji
dt = 0.1              # krok czasowy
nt = 500              # liczba kroków czasowych
Px, Py = 10, 10       # rozmiar plamki

def add_drop(row, col, radius=Px):
    global u
    row = int(row)
    col = int(col)
    # Generujemy siatkę wokół środka dropa
    x = np.arange(max(0, col-radius), min(Ny, col+radius))
    y = np.arange(max(0, row-radius), min(Nx, row+radius))
    X, Y = np.meshgrid(x, y)
    # Maska koła
    mask = (X - col)**2 + (Y - row)**2 <= radius**2
    u[max(0,row-radius):min(Nx,row+radius), max(0,col-radius):min(Ny,col+radius)][mask] = 1.0



def on_click(event):
    # czy współrzędne kliknięcia istnieją
    if event.xdata is not None and event.ydata is not None:
        add_drop(event.ydata, event.xdata)
        # start animacji
        ani.event_source.start()  # odblokowuje animację

def laplacian_loops(u):
    #Pobranie danych
    Nx, Ny = u.shape
    lap = np.zeros_like(u)

    #Pętla po wnętrzu siatki
    for i in range(1, Nx-1):
        for j in range(1, Ny-1):
            #Wzór na laplasjan w 2D - opisuje jak stężenie rozchodzi się w przestrzeni
            lap[i,j] = (u[i+1,j] + u[i-1,j] + u[i,j+1] + u[i,j-1] - 4*u[i,j]) / (dx*dx)
    return lap

def step_explicit(u, D, dt):
    lap = laplacian_loops(u)
    u_new = u + D * dt * lap
    #Nałóż warunki brzegowe Neumann - kopiuje stężenie na brzegu od najbliższego punktu wewnętrznego
    u_new[0, :] = u_new[1, :]
    u_new[-1, :] = u_new[-2, :]
    u_new[:, 0] = u_new[:, 1]
    u_new[:, -1] = u_new[:, -2]
    return u_new


# Inicjalizacja
u = np.zeros((Nx, Ny), dtype=float)

# Tworzenie animacji
fig, ax = plt.subplots()
im = ax.imshow(u, origin='lower', cmap='cool', vmin=0, vmax=1)
plt.colorbar(im, ax=ax, label='stężenie')
ax.set_title('Dyfuzja barwnika')

fig.canvas.mpl_connect('button_press_event', on_click)

def update(frame):
    global u
    u = step_explicit(u, D, dt)
    im.set_data(u)
    return [im]

ani = FuncAnimation(fig, update, frames=nt, blit=True, interval=30)
ani.event_source.stop()  # zatrzymujemy animację na początku
plt.show()
