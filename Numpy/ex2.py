import numpy as np

m = np.random.randint(-100, 101, size=(9,9), dtype=np.int32)

even = m[m % 2 == 0]
sortedeven = np.sort(even)

print(sortedeven)