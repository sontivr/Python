from itertools import groupby

n = int(input().strip())
nlist = sorted(list(map(int, input().strip().split())))

for k, g in groupby(nlist, lambda x: int(x)):
  if (len(list(g)) == 1):
    print(k)

'''
5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 
'''
