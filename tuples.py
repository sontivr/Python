if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    #print("n: {} integer_list: {}".format(n, list(integer_list)))
    #t = tuple(list(integer_list))
    print("{}".format(hash(tuple(list(integer_list)))))

