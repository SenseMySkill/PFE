import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

with open("pie.txt", "r") as r:
    file = r.read()

values = list(map(float, file.split()))

plt.pie(
    values,
    colors=cm.terrain(np.arange(0.0, 1.0,0.2)),
    wedgeprops={'edgecolor': 'black', 'linewidth': 1},
    explode=[0.03]*len(values)
)

plt.axis('equal')
plt.show()
