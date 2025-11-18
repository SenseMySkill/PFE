def gr2li(strings):
    count = 0

    for i in range(len(strings)):
        if len(strings[i]) > 2 and strings[i][0] == strings[i][-1]:
            count += 1

    return count

strings = [
    "aba",
    "xyz",
    "aa",
    "hello",
    "abcba",
    "ab",
    "xyzx",
    "x",
    "racecar",
    "noon"
]

print(gr2li(strings))

