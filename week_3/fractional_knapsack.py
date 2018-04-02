# Uses python3
import sys
from collections import namedtuple

Item = namedtuple('Item', ['weight', 'value', 'value_per_weight_unit'])


def get_optimal_value(knapsack_capacity, weights, values):
    value = 0.
    items = [Item(weight, values[i], values[i] / weight) for i, weight in enumerate(weights)]
    items = sorted(items, key=lambda _item: _item.value_per_weight_unit, reverse=True)
    for item in items:
        remaining_capacity = knapsack_capacity - item.weight
        weight_to_take_for_item = item.weight if remaining_capacity >= 0 else knapsack_capacity
        value += (weight_to_take_for_item * item.value_per_weight_unit)
        if remaining_capacity <= 0:
            break
        knapsack_capacity = remaining_capacity
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.3f}".format(opt_value))
