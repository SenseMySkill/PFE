import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

r = open("bars.txt", "r")
file = r.read()

coords = file.split("\n")
x = coords[0].split()
y = coords[1].split()

print(x)

for i in range(len(x)):
    x[i] = float(x[i])
    y[i] = float(y[i])

colors = [cm.copper(val) for val in y]

plt.bar(x,y, color=colors)

for xi, yi in zip(x,y):
    plt.text(xi - 0.3, yi + 0.02, yi)

plt.axis([0,12,0,1])

plt.show()