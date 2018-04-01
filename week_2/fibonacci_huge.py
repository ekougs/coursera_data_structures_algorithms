# Uses python3
import sys

import math


def pisano_period(n):
    if n == 2:
        return 3
    if n == 3:
        return 8
    return 2 * n if n % 2 == 0 else 4 * n


def calc_fib(n):
    if n <= 1:
        return n

    fibonnacci_results = [0, 1]
    for i in range(n - 1):
        current_fibonnacci_result = fibonnacci_results[0] + fibonnacci_results[1]
        fibonnacci_results[0] = fibonnacci_results[1]
        fibonnacci_results[1] = current_fibonnacci_result
    return fibonnacci_results[1]


if __name__ == '__main__':
    # raw_n_m = sys.stdin.read();
    # n, m = map(int, raw_n_m.split())
    n, m = 2816213588, 30524
    print(calc_fib(m))

    p_fib_m = pisano_period(calc_fib(m))
    print(p_fib_m)
    print(n % p_fib_m, p_fib_m, calc_fib(n % p_fib_m))
    print(calc_fib(n % p_fib_m) % m)
