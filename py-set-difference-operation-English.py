n = int(input().strip())
nset = set(list(map(int, input().strip().split())))
b = int(input().strip())
bset = set(list(map(int, input().strip().split())))
print(len(nset.difference(bset)))



'''
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
'''

