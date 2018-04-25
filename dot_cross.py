import numpy as np

A = []
B = []
A.append(np.array([int(x) for x in input().split()]))
B.append(np.array([int(x) for x in input().split()]))

print(A)
print(B)
print(np.inner(A, B)[0][0])
print(np.outer(A, B))
