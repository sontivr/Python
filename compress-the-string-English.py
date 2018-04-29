import itertools

data = input().strip()
for k, g in itertools.groupby(data, lambda x: int(x[0])):
    print("{} ".format(tuple((len(list(g)), k))), end='')
print()



'''
Sample Input

1222311
Sample Output

(1, 1) (3, 2) (1, 3) (2, 1)
Explanation

First, the character  occurs only once. It is replaced by . Then the character  occurs three times, and it is replaced by  and so on.

Also, note the single space within each compression and between the compressions.
'''
