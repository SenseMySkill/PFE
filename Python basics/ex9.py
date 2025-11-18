file = open("lista2.txt", "r")
plik = file.read()

plik = plik.replace("\n", " ")

slowa = plik.split()
uniquewords = list(set(slowa))

wynik = []

for word in uniquewords:
    wcount = slowa.count(word)
    wynik.append([word, wcount])

    while word in slowa:
        slowa.remove(word)



print(wynik)