import numpy as np

array = np.array([float(x) for x in input().split()])
#array = np.loadtxt(input(), dtype=np.int)
print(np.floor(array))
print(np.ceil(array))
print(np.rint(array))
