file = open("lista.txt", "r")
string = file.read()

lines = string.split('\n')

pairs = [line.strip().split('\t') for line in lines]

w = dict(pairs)

print(w)