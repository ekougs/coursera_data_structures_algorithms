# Uses python3
def calc_fib(n):
    if n <= 1:
        return n

    fibonnacci_results = [0, 1]
    for i in range(n - 1):
        current_fibonnacci_result = fibonnacci_results[0] + fibonnacci_results[1]
        fibonnacci_results[0] = fibonnacci_results[1]
        fibonnacci_results[1] = current_fibonnacci_result
    return fibonnacci_results[1]


n = int(input())
print(calc_fib(n))
