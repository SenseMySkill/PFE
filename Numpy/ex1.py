import numpy as np

a = np.random.uniform(0,100,25)

a[a.argmax()] = 200
a[a < 50] = 0

print(a)