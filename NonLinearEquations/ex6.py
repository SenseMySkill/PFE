import numpy as np

data = np.load("solve.npz")

print(data.files)

A = data['A']
b = data['b']

try:
    x = np.linalg.solve(A, b)
    print("Exact sol", x)
except np.linalg.LinAlgError:
    x, residuals, rank, s = np.linalg.lstsq(A, b, rcond=None)
    print("No exact solution", x)