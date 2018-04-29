


n = int(input().strip())
s = set(list(map(int, input().strip().split())))
N = int(input().strip())

for i in range(N):
  op = input().strip().split()
  if (len(op) == 1):
    cmd0 = "s.{}()".format(op[0]) 
  if (len(op) == 2):
    cmd0 = "s.{}({})".format(op[0], op[1])
  eval(cmd0)
print(sum(s))

'''
9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop 
discard 6
remove 5
pop 
discard 5
'''
