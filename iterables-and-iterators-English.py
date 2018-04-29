import itertools


n = int(input().strip())
a = input().strip().split()
k = int(input().strip())
ai = []
ai2 = []
[ai.append(i) for i in range(1, n+1)]
#print(ai)
[ai2.append(i) for i in range(1, n+1) if a[i-1] == 'a']
#print(ai2)

total_count = 0
intersect_count = 0
for index_combo in itertools.combinations(ai, k):
  #print(index_combo)
  total_count += 1
  if (set(index_combo).intersection(set(ai2)) != set()):
    intersect_count += 1

print("{}".format(round(intersect_count/total_count, 4)))

'''
Sample Input

4 
a a c d
2
Sample Output

0.8333
Explanation

All possible unordered tuples of length  comprising of indices from  to  are:


Out of these  combinations,  of them contain either index  or index  which are the indices that contain the letter ''.

Hence, the answer is 5/6.
'''
