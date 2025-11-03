def exchange(x, y):
    a = y[0:2] + x[2:]
    b = x[0:2] + y[2:]
    return a,b

print("Type in first string")
x = input()
print("Type in second string")
y = input()
print(exchange(x,y))