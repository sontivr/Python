# from itertools import permutations, combinations
from collections import defaultdict


def minion_game(string):
    # your code goes here
    # words = defaultdict(int)
    kevin_score = 0
    stuart_score = 0
    length = len(string)
    vowels = 'AEIOU'
    for i in range(length):
      if string[i] in vowels:
         kevin_score += length - i
      else:
         stuart_score += length - i

    if (kevin_score > stuart_score):
        print("Kevin {}".format(kevin_score))
    elif (kevin_score < stuart_score):
        print("Stuart {}".format(stuart_score))
    else:
        print("Draw")


'''
    # print(words)
    kevin_total = 0
    stuart_total = 0
    stuart_total = sum([v for k, v in words.items() if (k[0] not in 'AEIOU')])
    kevin_total = sum([v for k, v in words.items() if (k[0] in 'AEIOU')])
    if (kevin_total > stuart_total):
        print("Kevin {}".format(kevin_total))
    elif (kevin_total < stuart_total):
        print("Stuart {}".format(stuart_total))
    else:
        print("DRAW")
'''

if __name__ == '__main__':
    s = input()
    minion_game(s)

'''
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

For better understanding, see the image below:
'''
