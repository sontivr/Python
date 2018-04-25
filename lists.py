
if __name__ == '__main__':
    n = int(input())
    d = list()
    for _ in range(n):
        cmd = input().split()
        if(len(cmd) == 2):
          cmd0 = "d.{}({})".format(cmd[0], int(cmd[1]))

        if(len(cmd) == 3):
          cmd0 = "d.{}({},{})".format(cmd[0], int(cmd[1]), int(cmd[2]))

        if(len(cmd) == 1):
           if cmd[0] == 'print':
              cmd0 = "{}(d)".format(cmd[0])
           else:
              cmd0 = "d.{}()".format(cmd[0])


        eval(cmd0)
    #print(*d)
