import re

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
matrix = []
matrix_i = 0
for matrix_i in range(n):
    matrix_t = str(input())
    matrix.append(matrix_t)

matrix_p = ''.join([''.join(s) for s in zip(*matrix)])
print(re.sub(r'([A-Za-z0-9])[!@#$%&\s]+([A-Za-z0-9])', '\\1 \\2', matrix_p))



'''
7 3
Tsi
h%x
i #
sM 
$a 
#t%
ir!
'''
