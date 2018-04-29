from itertools import combinations

inlist = input().strip().split()
for i in range(1, int(inlist[1])+1):
  [print(''.join(i)) for i in combinations(sorted(inlist[0]), i)]

'''
HACK 2

A
C
H
K
AC
AH
AK
CH
CK
HK
'''
