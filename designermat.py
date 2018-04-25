
'''
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be N x M. (N is an odd natural number, and M is 3 times N.)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
'''

def print_welcome(width, length):
  #print('Size: {} x {}'.format(width, length))
  dash = '-'
  dbar = '.|.'
  middle = 'WELCOME'
  for i in range(width):
    if (i % 2 == 1):
      print((i*dbar).center(length, dash).rjust(length))
  print(middle.center(length, dash).rjust(length))
  for i in reversed(range(width)):
    if (i % 2 == 1):
      print((i*dbar).center(length, dash).rjust(length))




if __name__ == '__main__':
   n, m = [ int(i) for i in input().split()]
   #print('Size: {} x {} Type: {} x {}'.format(n, m, type(n), type(m)))
   if ( n < 101 and n > 5):
     print_welcome(n, m)
   #print_welcome(7, 21)


'''
    Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    
    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------
'''
