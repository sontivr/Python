from itertools import permutations


inlist = input().strip().split()
[print(''.join(i)) for i in permutations(sorted(inlist[0]), int(inlist[1]))]

'''
HACK 2

AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH
'''
