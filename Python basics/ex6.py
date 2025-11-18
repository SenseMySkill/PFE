def func(strings):
    w = []
    w2 = []
    for i in range(len(strings)):
        if strings[i][0] == "x":
            w.append(strings[i])
        else:
            w2.append(strings[i])

    w = sorted(w)
    w2 = sorted(w2)

    w = w+w2

    return w


strings = [
    "apple", "xenon", "banana", "xylophone", "orange", "xerox", "grape", "xavier"
]

print(func(strings))