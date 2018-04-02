# Uses python3

import sys


def max_dot_product(list_a, list_b):
    # write your code here
    list_a = sorted(list_a)
    list_b = sorted(list_b)
    res = 0
    for a, b in zip(list_a, list_b):
        res += a * b
    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
