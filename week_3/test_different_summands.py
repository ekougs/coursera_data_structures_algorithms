from week_3.different_summands import optimal_summands


def test_summands_for_1_are_1():
    # GIVEN
    n = 1

    # WHEN
    summands = optimal_summands(n)

    # THEN
    assert summands == [1]


def test_summands_for_2_are_2():
    # GIVEN
    n = 2

    # WHEN
    summands = optimal_summands(n)

    # THEN
    assert summands == [2]


def test_summands_for_6_are_1_2_3():
    # GIVEN
    n = 6

    # WHEN
    summands = optimal_summands(n)

    # THEN
    assert summands == [1, 2, 3]


def test_summands_for_8_are_1_2_5():
    # GIVEN
    n = 8

    # WHEN
    summands = optimal_summands(n)

    # THEN
    assert summands == [1, 2, 5]


def test_change_for_10_are_1_2_3_4():
    # GIVEN
    n = 10

    # WHEN
    summands = optimal_summands(n)

    # THEN
    assert summands == [1, 2, 3, 4]
