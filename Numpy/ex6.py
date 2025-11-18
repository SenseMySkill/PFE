import numpy as np
import matplotlib.pyplot as plt


data = np.genfromtxt("populacje.txt", delimiter='\t', skip_header=1)

years = data[:,0]
rabbits = data[:,1]
foxes = data[:,2]
carrots = data[:,3]

#1

def top3increase(dane, years):
    diff = dane[1:] - dane[:-1]
    increase = np.where(diff > 0, diff, 0)
    top3id = np.argsort(increase)[-3:][::-1]
    top3_years = years[1:][top3id]
    top3_val = increase[top3id]
    return list(zip(top3_years, top3_val))

print("\n=================1=================\n")
print("Króliki: ", top3increase(rabbits, years))
print("Lisy:", top3increase(foxes, years))
print("Marchewki", top3increase(carrots, years))

#2
print("\n=================2=================\n")

totalpop = rabbits + foxes + carrots
difftotal = totalpop[1:] - totalpop[:-1]
diffrabb = rabbits[1:] - rabbits[:-1]

mask = (difftotal < 0) & (diffrabb > 0)

print("Lata: ", years[1:][mask])

#3
print("\n=================3=================\n")

pop_matrix = np.vstack([rabbits, foxes]).T

dominant_idx = np.argmax(pop_matrix, axis=1)

species = np.array(['rabbits', 'foxes'])
dominant_species = species[dominant_idx]

dom = list(zip(years, dominant_species))

print(dom)

#4
print("\n=================4=================\n")

max_len = 1
current_len = 1
streak_species = dominant_species[0]
start_year = years[0]
best_start = years[0]
best_end = years[0]

for i in range(1, len(dominant_species)):
    if dominant_species[i] == dominant_species[i-1]:
        current_len += 1
    else:
        current_len = 1
        start_year = years[i]
    if current_len > max_len:
        max_len = current_len
        streak_species = dominant_species[i]
        best_start = start_year
        best_end = years[i]

print(streak_species, best_start, best_end, max_len)

#5
print("\n=================5=================\n")

percent_dominance = {}

total_years = len(dominant_species)

for sp in species:
    dominant_years = np.sum(dominant_species == sp)
    percent = 100 * dominant_years / total_years
    percent_dominance[sp] = percent

for sp, perc in percent_dominance.items():
    print(f"{sp}: {perc:.2f}%")
