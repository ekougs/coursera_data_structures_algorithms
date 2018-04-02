# Uses python3
import sys


def optimal_summands(n):
    summands = []
    sum = 0
    for i in range(1, n + 1):
        if 0 < n - (sum + i) <= i:
            continue
        sum += i
        summands.append(i)
        if sum == n:
            break
    return summands


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
