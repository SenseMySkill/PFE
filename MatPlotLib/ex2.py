import matplotlib.pyplot as plt
from matplotlib import cm

r = open("scatter.txt", "r")
file = r.read()

coords = file.split("\n")
x = coords[0].split()
y = coords[1].split()

for i in range(len(x)):
    x[i] = float(x[i])
    y[i] = float(y[i])

ax = plt.axes(polar=True)
ax.set_facecolor('lightgrey')
ax.set_ylim(-1, 1.4)

colors = y

plt.scatter(x,y, c=colors, cmap=cm.jet, s=7)

plt.show()