from week_3.dot_product import max_dot_product


def test_max_product_of_2_unordered_lists_containing_negative_numbers():
    # GIVEN
    list_a = [1, 3, -5]
    list_b = [-2, 4, 1]

    # WHEN
    max_product = max_dot_product(list_a, list_b)

    # THEN
    assert max_product == 23


def test_max_product_is_0_for_empty_lists():
    # GIVEN
    list_a = []
    list_b = []

    # WHEN
    max_product = max_dot_product(list_a, list_b)

    # THEN
    assert max_product == 0
