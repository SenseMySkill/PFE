import numpy as np
import matplotlib.pyplot as plt

def A_of(p):
    sp = np.sqrt(p)
    return np.array([[1.0, sp],
                     [1.0, 1.0/sp]])

p1 = np.linspace(0.9,0.999, 400)
p2 = np.linspace(1.001, 1.1, 400)
p = np.concatenate([p1, p2])

conds = []

for pp in p:
    A = A_of(pp)
    conds.append(np.linalg.cond(A, 2))
conds = np.array(conds)

plt.figure(figsize=(8,5))
plt.semilogy(p, conds, lw=2)
plt.axvline(1.0, color='gray', linestyle='--', label='p = 1 (singular)')
plt.show()