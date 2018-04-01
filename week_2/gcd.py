# Uses python3
import sys


def gcd(a, b):
    smallest = a if a <= b else b
    greatest = a if a > b else b
    if smallest == 0:
        return greatest
    mod = greatest % smallest
    return gcd(smallest, mod)


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(a, b))
