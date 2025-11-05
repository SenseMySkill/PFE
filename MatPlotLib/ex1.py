import matplotlib.pyplot as plt

x = [3,7,10,12]
y = [3,8,1,9]

plt.plot(x,y, label = 'funkcja', linestyle="dashed", marker="o", color="blue")

plt.legend()

plt.xlim(50,100)
plt.xticks([1,3,5,9])

plt.ylim(3.8,7.9)
plt.yticks([3,7,2,9])

plt.axis([0,15,0,15])

plt.xlabel("X Parameter")
plt.ylabel("Y Parameter")

plt.title("Wykres")

plt.savefig("ex1.png")