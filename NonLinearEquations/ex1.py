import matplotlib.pyplot as plt
import numpy as np

A = np.array([[0.2, -1], [0.5, -1]])
b = np.array([0, 3])

x = np.linalg.solve(A,b)

print(x)

czas = np.linspace(0, 20, 200)
twoja_droga = 0.2*czas
konska_droga = 0.5*(czas-6)
konska_droga[czas<6] = 0  # koń jeszcze nie rusza

plt.plot(czas, twoja_droga, label='Ty')
plt.plot(czas, konska_droga, label='Koń')
plt.show()

