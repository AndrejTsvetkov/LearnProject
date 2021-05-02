from _collections import OrderedDict

n = int(input())
a = [int(i) for i in input().split()]

def f_rec(n):
    dict = OrderedDict({0: 0, 1: 1, 2: 2})
    if n in dict.keys():
        return dict[n]
    else:
        for i in range(3, n + 1):
            current_value = dict[i-1] + dict[i-3]
            dict.popitem(last = False)
            dict[i] = current_value
        return dict[n]



for i in a:
    print(f_rec(i), end=' ')
