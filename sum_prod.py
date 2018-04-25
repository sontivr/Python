import numpy as np

n, m = [int(x) for x in input().split()]

array = []
for i in range(n):
  array.append(np.array([int(x) for x in input().split()]))

print(np.array(array))
print(np.sum(array, 0))
print(np.product(np.sum(array, 0)))

