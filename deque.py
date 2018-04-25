from collections import deque

if __name__ == '__main__':
    n = int(input())
    commands = list()
    d = deque()
    for _ in range(n):
        cmd = input().split()
        if(len(cmd) == 2):
          cmd0 = "d.{}({})".format(cmd[0], cmd[1])
        else:
          cmd0 = "d.{}()".format(cmd[0])
        eval(cmd0)
    print(*d)
