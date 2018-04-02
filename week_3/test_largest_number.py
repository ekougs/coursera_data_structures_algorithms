# Uses python3
from week_3.largest_number import largest_number, LargestNumberKey


def test_key_2_is_gt_key_21():
    # GIVEN
    key_2 = LargestNumberKey('2')
    key_21 = LargestNumberKey('21')

    # WHEN

    # THEN
    assert key_2 > key_21


def test_key_23_is_gt_key_2():
    # GIVEN
    key_23 = LargestNumberKey('23')
    key_2 = LargestNumberKey('2')

    # WHEN

    # THEN
    assert key_23 > key_2


def test_key_21_is_lt_key_2():
    # GIVEN
    key_2 = LargestNumberKey('2')
    key_21 = LargestNumberKey('21')

    # WHEN

    # THEN
    assert key_21 < key_2


def test_key_2_is_ge_key_21():
    # GIVEN
    key_2 = LargestNumberKey('2')
    key_21 = LargestNumberKey('21')

    # WHEN

    # THEN
    assert key_2 >= key_21


def test_key_21_is_le_key_2():
    # GIVEN
    key_2 = LargestNumberKey('2')
    key_21 = LargestNumberKey('21')

    # WHEN

    # THEN
    assert key_21 <= key_2


def test_key_22_is_eq_key_2():
    # GIVEN
    key_2 = LargestNumberKey('2')
    key_22 = LargestNumberKey('22')

    # WHEN

    # THEN
    assert key_22 == key_2


def test_key_22_is_le_key_2():
    # GIVEN
    key_2 = LargestNumberKey('2')
    key_22 = LargestNumberKey('22')

    # WHEN

    # THEN
    assert key_22 <= key_2


def test_key_22_is_ge_key_2():
    # GIVEN
    key_2 = LargestNumberKey('2')
    key_22 = LargestNumberKey('22')

    # WHEN

    # THEN
    assert key_22 >= key_2


def test_for_2_21_is_221():
    # GIVEN
    numbers = ['2', '21']

    # WHEN
    largest_num = largest_number(numbers)

    # THEN
    assert largest_num == '221'


def test_for_2_23_is_232():
    # GIVEN
    numbers = ['23', '2']

    # WHEN
    largest_num = largest_number(numbers)

    # THEN
    assert largest_num == '232'


def test_for_9_4_6_1_9_is_99641():
    # GIVEN
    numbers = ['9', '4', '6', '1', '9']

    # WHEN
    largest_num = largest_number(numbers)

    # THEN
    assert largest_num == '99641'


def test_for_23_39_92_is_923923():
    # GIVEN
    numbers = ['23', '39', '92']

    # WHEN
    largest_num = largest_number(numbers)

    # THEN
    assert largest_num == '923923'
