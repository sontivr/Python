from itertools import product

k, m = map(int, input().strip().split())
klist = (list(map(int, input().strip().split()))[1:] for _ in range(k))
print(max(map(lambda x: sum(i**2 for i in x)%m, product(*klist))))


'''
3 1000
2 5 4
3 7 8 9 
5 5 7 8 9 10 
'''
