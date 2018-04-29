

n, m = map(int, input().strip().split())
nlist = list(map(int, input().strip().split()))
a = set(list(map(int, input().strip().split())))
b = set(list(map(int, input().strip().split())))

happiness = sum([1 for i in nlist if (a.intersection({i}) == {i})])
happiness -= sum([1 for i in nlist if (b.intersection({i}) == {i})])
print(happiness)

'''
3 2
1 5 3
3 1
5 7
'''
