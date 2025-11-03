def intstrconv(y):
    x = int(y)
    if x <=9:
        print("The number of cookies is:", x)
    else:
        print("Too many cookies")

print("Type in the number of cookies")
x = input()
intstrconv(x)