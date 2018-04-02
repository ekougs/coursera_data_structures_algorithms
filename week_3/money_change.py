# Uses python3
import sys

_change_values = [10, 5, 1]


def get_change(amount):
    min_number_of_coins = 0
    for change_value in _change_values:
        min_number_of_coins += amount // change_value
        amount = amount % change_value
        if amount == 0:
            break
    return min_number_of_coins


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
