# Uses python3
import sys


def gcd(a, b):
    smallest = a if a <= b else b
    greatest = a if a > b else b
    if smallest == 0:
        return greatest
    mod = greatest % smallest
    return gcd(smallest, mod)


def lcm(a, b):
    return a * int(b / gcd(a, b))


if __name__ == '__main__':
    raw_a_b = sys.stdin.read()
    a, b = map(int, raw_a_b.split())
    print(lcm(a, b))
