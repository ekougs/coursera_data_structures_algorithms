from week_3.money_change import get_change


def test_change_for_zero():
    # GIVEN
    amount = 0

    # WHEN
    min_number_of_coins = get_change(amount)

    # THEN
    assert min_number_of_coins == 0


def test_change_for_2():
    # GIVEN
    amount = 2

    # WHEN
    min_number_of_coins = get_change(amount)

    # THEN
    assert min_number_of_coins == 2


def test_change_for_28():
    # GIVEN
    amount = 28

    # WHEN
    min_number_of_coins = get_change(amount)

    # THEN
    assert min_number_of_coins == 6
