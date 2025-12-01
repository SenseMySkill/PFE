import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

alpha = 1.0
beta = 0.1
gamma = 1.5
delta = 0.075
K = 50.0

x0 = 10
y0 = 5
y0_vec = [x0, y0]

t = np.linspace(0, 200, 5000)

def classic(t, z):
    x, y = z
    dx = alpha*x - beta*x*y
    dy = delta*x*y - gamma*y
    return [dx, dy]

def logistic(t, z):
    x, y = z
    dx = alpha*x*(1 - x/K) - beta*x*y
    dy = delta*x*y - gamma*y
    return [dx, dy]

sol_classic = solve_ivp(classic, [t[0], t[-1]], y0_vec, t_eval=t)
sol_logistic = solve_ivp(logistic, [t[0], t[-1]], y0_vec, t_eval=t)

xc = sol_classic.y[0]
yc = sol_classic.y[1]
xl = sol_logistic.y[0]
yl = sol_logistic.y[1]

plt.figure(figsize=(12,6))
plt.plot(t, xc, label='Prey classic')
plt.plot(t, yc, label='Pred classic')
plt.plot(t, xl, label='Prey logistic (K)')
plt.plot(t, yl, label='Pred logistic (K)')
plt.xlabel("Time")
plt.ylabel("Population")
plt.title("Classic vs Logistic-prey Predator-Prey System")
plt.legend()
plt.grid(True)
plt.show()

print("Finite K reduces prey overshoot, damps oscillations, lowers amplitudes, and can stabilize long-term dynamics compared to the classic undamped oscillatory system.")
