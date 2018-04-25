

if __name__ == '__main__':
   x, k = input().strip().split()
   if eval(input().strip().replace("x", x)) == int(k):
     print("True")
   else:
     print("False")


#1 4
#x**3 + x**2 + x + 1
