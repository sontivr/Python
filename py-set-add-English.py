
n = int(input().strip())
myset = set()
[myset.add(input().strip()) for _ in range(n)]
print(len(myset))


'''
7
UK
China
USA
France
New Zealand
UK
France 
'''
