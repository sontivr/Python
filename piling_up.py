from collections import deque

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        cubes = int(input())
        lengths = deque(map(int, list(input().split())))
        #print("cubes: {} lengths: {} min: {} max: {} len: {}".format(cubes, lengths, min(lengths), max(lengths), len(lengths)))
        count = len(lengths)
        i = 0
        top = 0
        while i <= count:
          if (count == 0):
              print("Yes")
              break
          #print("lengths: {}".format(lengths))
           
          if (lengths[0] > lengths[-1]):
             curmax = lengths[0]
             popped = lengths.popleft()
          else:
             curmax = lengths[-1]
             popped = lengths.pop()
          count -= 1

          if top == 0:
             top = curmax
          elif (top >= curmax):
             top = curmax
          else:
             break

          #print("popped: {} count: {} top: {} i: {} maxlen: {}".format(popped, count, top, i, lengths.maxlen))
        if (count > 0):
          print("No")
