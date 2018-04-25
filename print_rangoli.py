from string import ascii_lowercase
'''
'''

def print_rangoli(number):
  length = 4 * (number - 1) + 1
  dash = '-'
  left = ''
  rlist = []
  for i in reversed(ascii_lowercase[:number]):
    str = left + i + left[::-1]
    print(str.center(length, dash))
    rlist.append(str.center(length, dash))
    left += i + dash

  for i in reversed(range(len(rlist)-1)):
    print(rlist[i])



if __name__ == '__main__':
   n = int(input())
   print_rangoli(n)


'''
#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

'''
