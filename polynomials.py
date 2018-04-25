import numpy as np

A = [float(x) for x in input().split()]
X = float(input())
print(np.polyval(np.poly1d(A), X))
