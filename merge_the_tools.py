from collections import OrderedDict

def merge_the_tools(string, k):
    # your code goes here
    length = len(string)
    seg_count = length/k
    for i in range(length):
      if (i % k == 0):
        print(''.join(OrderedDict.fromkeys(string[i:k+i])))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
