import matplotlib.pyplot as plt
import numpy as np

x = [0, 10, 20, 30, 40]
y = [0, 23, 26, 28, 30]

plt.plot(x, y,
         linestyle="-.",
         color="red",
         marker="o",
         markerfacecolor="blue",
         markeredgecolor="red",
         markeredgewidth=1,
         linewidth=4,
         markersize=12
         )

plt.grid(visible=True)

plt.xticks(np.arange(0, 41, 1))
plt.yticks(np.arange(0, 31, 1))
plt.tick_params(labelbottom=False, labelleft=False)

plt.axis([0,40,0,30])

plt.show()