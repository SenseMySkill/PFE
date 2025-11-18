def func(numbers):
    w = []
    last = None
    for i in range(len(numbers)):
        if numbers[i] != last:
            w.append(numbers[i])
        last = numbers[i]

    return w

numbers = [
    1, 2, 2, 3, 3, 3, 4, 5, 5, 3, 3, 6, 6, 7, 8, 8, 9
]

print(func(numbers))