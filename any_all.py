


if __name__ == '__main__':
   n = int(input().strip())
   mylist = list(map(int, input().split()))
   print(mylist)
   mylist2 = []
   #print(list(map(lambda x: int(str(x)[::-1]), mylist)))
   #print(set(mylist).intersection(set(list(map(lambda x: int(str(x)[::-1]), mylist)))))
   #mylist2 = list(map(lambda x: ("{}>0".format(x)).replace("'", ""), mylist))
   mylist2 += list(map(lambda x: "{}>0".format(x), mylist)).strip("'")
   #mylist3 = ('[' + ', '.join(mylist2) + ']')
   print(mylist2)

'''
Task

You are given a space separated list of integers. If all the integers are positive, then you need to check if any integer is a palindromic integer.

Input Format

The first line contains an integer .  is the total number of integers in the list. 
The second line contains the space separated list of  integers.

Constraints


Output Format

Print True if all the conditions of the problem statement are satisfied. Otherwise, print False.

Sample Input

5
12 9 61 5 14 
Sample Output

True
'''

