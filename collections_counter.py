from collections import Counter

if __name__ == '__main__':
    shoe_count = int(input())
    sizes_list = map(int, input().split())
    cust_count = int(input())
    size_price = []

    for _ in range(cust_count):
       size_price.append(list(map(int, input().split())))

    print("{}".format(Counter(size_price).elements()))

