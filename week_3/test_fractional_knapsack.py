import pytest

from week_3.fractional_knapsack import get_optimal_value


def test_optimal_value_for_3_unordered_items():
    # GIVEN
    weight = 50
    weights = [20, 50, 30]
    values = [60, 100, 120]

    # WHEN
    optimal_value = get_optimal_value(weight, weights, values)

    # THEN
    assert optimal_value == 180.


def test_optimal_value_for_3_unordered_items_and_fractional_for_one_item():
    # GIVEN
    weight = 60
    weights = [20, 50, 30]
    values = [60, 100, 120]

    # WHEN
    optimal_value = get_optimal_value(weight, weights, values)

    # THEN
    assert optimal_value == 200.


def test_optimal_value_for_1_item():
    # GIVEN
    weight = 10
    weights = [30]
    values = [500]

    # WHEN
    optimal_value = get_optimal_value(weight, weights, values)

    # THEN
    assert pytest.approx(optimal_value, 0.0001) == 166.6667


def test_optimal_value_for_0_weight():
    # GIVEN
    weight = 0
    weights = [30]
    values = [500]

    # WHEN
    optimal_value = get_optimal_value(weight, weights, values)

    # THEN
    assert optimal_value == 0.


def test_optimal_value_for_0_item():
    # GIVEN
    weight = 20
    weights = []
    values = []

    # WHEN
    optimal_value = get_optimal_value(weight, weights, values)

    # THEN
    assert optimal_value == 0.


def test_optimal_value_for_weight_over_3_unordered_items():
    # GIVEN
    weight = 110
    weights = [20, 50, 30]
    values = [60, 100, 120]

    # WHEN
    optimal_value = get_optimal_value(weight, weights, values)

    # THEN
    assert optimal_value == 280.
