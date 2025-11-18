import matplotlib.pyplot as plt

r = open("data3.dat", "r")
file = r.read()

file = file.split("\n")

x = list(map(float, file[0].split(",")))
y = list(map(float, file[1].split(",")))
z = list(map(float, file[2].split(",")))

fig = plt.figure(figsize=(16,9))

plt.boxplot([x,y,z])

plt.show()