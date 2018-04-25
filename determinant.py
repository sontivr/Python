import numpy as np

n = int(input())

array = []
for i in range(n):
  array.append(np.array([float(x) for x in input().split()]))

print(np.array(array))
print(np.linalg.det(array))
