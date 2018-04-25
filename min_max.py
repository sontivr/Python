import numpy as np

n, m = [int(x) for x in input().split()]

array = []
for i in range(n):
  array.append(np.array([int(x) for x in input().split()]))

print(np.array(array))
print(np.min(array, 1))
print(np.max(np.min(array, 1)))

