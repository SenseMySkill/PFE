import matplotlib.pyplot as plt

with open("pie.txt", "r") as r:
    file = r.read()

values = list(map(float, file.split()))

fig = plt.figure(figsize=(10,4))

ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)

ax1.hist(values, bins=30, cumulative=True, density=True)

ax2.hist(values, bins=30, cumulative=False, density=True)

plt.show()