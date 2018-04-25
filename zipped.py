



if __name__ == '__main__':
   n, x = list(map(int, input().split()))
   marks = list()
   for i in range(x):
      marks.append(list(map(float, input().split())))
   print(marks)
   print(*zip(*marks))
   mylist = list(zip(*marks))
   for i in range(len(mylist)):
      print(sum(mylist[i])/len(mylist[i]))
      #print(mylist[i])

