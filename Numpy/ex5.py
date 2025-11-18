import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("populacje.txt", delimiter='\t', skip_header=1)

years = data[:,0]
rabbits = data[:,1]
foxes = data[:,2]
carrots = data[:,3]

print(np.mean(rabbits), np.mean(foxes), np.mean(carrots))
print(np.std(rabbits), np.std(foxes), np.std(carrots))

print(years[np.argmax(rabbits)], years[np.argmax(foxes)], years[np.argmax(carrots)])

for i in range(len(years)):
    if rabbits[i] > foxes[i] and rabbits[i] > carrots[i]:
        print(years[i], "Rabbits")
    elif foxes[i] > rabbits[i] and foxes[i] > carrots[i]:
        print(years[i], "Foxes")
    else:
        print(years[i], "Carrots")

ansr=[]
ansf=[]
ansc=[]

for i in range(len(years)):
    if rabbits[i] > 50000:
        ansr.append(years[i])

    if foxes[i] > 50000:
        ansf.append(years[i])

    if carrots[i] > 50000:
        ansc.append(years[i])

print(ansr)
print(ansf)
print(ansc)

x = years
y1 = rabbits
y2 = foxes
y3 = carrots

plt.plot(x, y1, label="Rabbits")
plt.plot(x, y2, label="Foxes")
plt.plot(x, y3, label="Carrots")

plt.legend()
plt.show()

rabbit_diff = np.diff(rabbits)
foxes_for_corr = foxes[1:]
corr = np.corrcoef(rabbit_diff, foxes_for_corr)[0,1]
print(corr)
