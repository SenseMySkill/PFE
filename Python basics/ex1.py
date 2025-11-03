def greeting(x):
    if isinstance(x, str) and x:
        print("Hello", x)
    else:
        print("Who is it?")


print("What's your name?")
x = input()
greeting(x)
