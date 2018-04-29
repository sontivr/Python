

m = int(input().strip())
mset = set(list(map(int, input().strip().split())))
n = int(input().strip())
nset = set(list(map(int, input().strip().split())))

[print(i) for i in sorted(mset.union(nset).difference(mset.intersection(nset)))]

print(mset)
print(nset)

