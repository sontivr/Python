


if __name__ == '__main__':
   n, m = list(map(int, input().split()))
   mylist = []
   for _ in range(n):
     mylist.append(list(map(int, input().split())))
   k = int(input().strip())
   [print(*k) for k in sorted(mylist, key=lambda athlete: athlete[k])]
   

'''
Sample Input 0

5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1
Sample Output 0

7 1 0
10 2 5
6 5 9
9 9 9
1 23 12

'''
