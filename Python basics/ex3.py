def deletetwo(x):
    return x[1:-1] if len(x) > 1 else 'Too short'

print("Type in anything")
x = input()
print(deletetwo(x))