if __name__ == '__main__':
    slist = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        slist.append([name, score])
    #print(slist)
    slist.sort(key=lambda x: float(x[1]))
    #print(slist)
    #print(sorted(list(set([x[1] for x in slist])))[1])
    #sorted(list(set([x[1] for x in slist])))[1])
    [print(x) for x in sorted([y[0] for y in slist if(y[1] == sorted(list(set([x[1] for x in slist])))[1])])]
