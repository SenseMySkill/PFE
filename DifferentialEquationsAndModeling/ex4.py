import numpy as np
import matplotlib.pyplot as plt

beta = 0.5
gamma = 0.1
S0 = 1000.0
I0 = 1.0
R0 = 0.0
T = 200.0
dt = 0.1
steps = int(T / dt) + 1
t = np.linspace(0, T, steps)

S = np.zeros(steps)
I = np.zeros(steps)
R = np.zeros(steps)
S[0], I[0], R[0] = S0, I0, R0

for n in range(steps - 1):
    N = S[n] + I[n] + R[n]
    dS = -beta * S[n] * I[n] / N
    dI = beta * S[n] * I[n] / N - gamma * I[n]
    dR = gamma * I[n]
    S[n+1] = S[n] + dS * dt
    I[n+1] = I[n] + dI * dt
    R[n+1] = R[n] + dR * dt

idx_peak = np.argmax(I)
day_peak = t[idx_peak]
peak_infected = I[idx_peak]

print(f"beta={beta}, gamma={gamma}")
print(f"Peak infected at day {day_peak:.2f} with {peak_infected:.0f} infected")

plt.figure(figsize=(10,6))
plt.plot(t, S, label='S')
plt.plot(t, I, label='I')
plt.plot(t, R, label='R')
plt.xlabel("Time (days)")
plt.ylabel("Number of people")
plt.title("SIR model (Forward Euler)")
plt.legend()
plt.grid(True)
plt.show()

print("beta = infection/contact rate (how quickly susceptible become infected)")
print("gamma = recovery rate (rate infected move to recovered)")
print("N is S+I+R because the model assumes a closed population with no births/deaths/migration")

beta2 = beta / 3.0
S2 = np.zeros(steps)
I2 = np.zeros(steps)
R2 = np.zeros(steps)
S2[0], I2[0], R2[0] = S0, I0, R0

for n in range(steps - 1):
    N2 = S2[n] + I2[n] + R2[n]
    dS2 = -beta2 * S2[n] * I2[n] / N2
    dI2 = beta2 * S2[n] * I2[n] / N2 - gamma * I2[n]
    dR2 = gamma * I2[n]
    S2[n+1] = S2[n] + dS2 * dt
    I2[n+1] = I2[n] + dI2 * dt
    R2[n+1] = R2[n] + dR2 * dt

idx_peak2 = np.argmax(I2)
day_peak2 = t[idx_peak2]
peak_infected2 = I2[idx_peak2]

print(f"After reducing beta by factor 3 (beta={beta2:.4f}):")
print(f"Peak infected at day {day_peak2:.2f} with {peak_infected2:.0f} infected")

plt.figure(figsize=(10,6))
plt.plot(t, I, label=f'I (beta={beta})')
plt.plot(t, I2, label=f'I (beta={beta2:.4f})')
plt.xlabel("Time (days)")
plt.ylabel("Infected")
plt.title("Effect of reducing beta on infection curve")
plt.legend()
plt.grid(True)
plt.show()

print("Observation: reducing beta delays the peak and lowers the maximum number of infected (flattens the curve).")
print("Real-world analogy: reducing contact rate via social distancing, mask-wearing, lockdowns, or reducing transmission probability per contact via vaccination/ventilation.")
print("Example: social distancing and mask mandates during a respiratory outbreak reduce effective beta and flatten the epidemic peak.")
