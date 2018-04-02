from week_3.covering_segments import Segment, optimal_points


def test_optimal_segments_for_segments_with_only_one_intersection():
    # GIVEN
    segments = [Segment(1, 3), Segment(2, 5), Segment(3, 6)]

    # WHEN
    points = optimal_points(segments)

    # THEN
    assert not [segment for segment in segments if not _is_covered(segment, points)]


def test_optimal_segments_for_segments_with_two_intersections():
    # GIVEN
    segments = [Segment(4, 7), Segment(1, 3), Segment(2, 5), Segment(5, 6)]

    # WHEN
    points = optimal_points(segments)

    # THEN
    assert not [segment for segment in segments if not _is_covered(segment, points)]


def test_optimal_segments_for_5_segments_and_two_intersections():
    # GIVEN
    segments = [Segment(4, 7), Segment(4, 5), Segment(1, 3), Segment(2, 5), Segment(6, 7)]

    # WHEN
    points = optimal_points(segments)

    # THEN
    assert not [segment for segment in segments if not _is_covered(segment, points)]


def test_optimal_segments_for_5_segments_and_three_intersections():
    # GIVEN
    segments = [Segment(4, 9), Segment(5, 6), Segment(1, 3), Segment(7, 8)]

    # WHEN
    points = optimal_points(segments)

    # THEN
    assert not [segment for segment in segments if not _is_covered(segment, points)]


def test_optimal_segments_for_100_segments():
    # GIVEN
    segments = [
        Segment(41, 42), Segment(52, 52), Segment(63, 63), Segment(80, 82), Segment(78, 79), Segment(35, 35), Segment(22, 23),
        Segment(31, 32), Segment(44, 45), Segment(81, 82), Segment(36, 38), Segment(10, 12), Segment(1, 1), Segment(23, 23),
        Segment(32, 33), Segment(87, 88), Segment(55, 56), Segment(69, 71), Segment(89, 91), Segment(93, 93), Segment(38, 40),
        Segment(33, 34), Segment(14, 16), Segment(57, 59), Segment(70, 72), Segment(36, 36), Segment(29, 29), Segment(73, 74),
        Segment(66, 68), Segment(36, 38), Segment(1, 3), Segment(49, 50), Segment(68, 70), Segment(26, 28), Segment(30, 30),
        Segment(1, 2), Segment(64, 65), Segment(57, 58), Segment(58, 58), Segment(51, 53), Segment(41, 41), Segment(17, 18),
        Segment(45, 46), Segment(4, 4), Segment(0, 1), Segment(65, 67), Segment(92, 93), Segment(84, 85), Segment(75, 77),
        Segment(39, 41), Segment(15, 15), Segment(29, 31), Segment(83, 84), Segment(12, 14), Segment(91, 93), Segment(83, 84),
        Segment(81, 81), Segment(3, 4), Segment(66, 67), Segment(8, 8), Segment(17, 19), Segment(86, 87), Segment(44, 44),
        Segment(34, 34), Segment(74, 74), Segment(94, 95), Segment(79, 81), Segment(29, 29), Segment(60, 61), Segment(58, 59),
        Segment(62, 62), Segment(54, 56), Segment(58, 58), Segment(79, 79), Segment(89, 91), Segment(40, 42), Segment(2, 4),
        Segment(12, 14), Segment(5, 5), Segment(28, 28), Segment(35, 36), Segment(7, 8), Segment(82, 84), Segment(49, 51),
        Segment(2, 4), Segment(57, 59), Segment(25, 27), Segment(52, 53), Segment(48, 49), Segment(9, 9), Segment(10, 10),
        Segment(78, 78), Segment(26, 26), Segment(83, 84), Segment(22, 24), Segment(86, 87), Segment(52, 54), Segment(49, 51),
        Segment(63, 64), Segment(54, 54)
    ]

    # WHEN
    points = optimal_points(segments)

    # THEN
    print(points)
    # Original solution
    # points = sorted([
    #     43, 1, 4, 5, 8, 9, 10, 14, 15, 18, 23, 26, 28, 29, 30, 32, 34, 35, 36, 40, 41, 44, 46, 49, 52, 54, 56, 58, 61, 62, 63,
    #     65, 67, 70, 74, 77, 78, 79, 81, 84, 87, 91, 93, 95
    # ])
    assert not [segment for segment in segments if not _is_covered(segment, points)]


def _is_covered(segment, points):
    for point in points:
        if segment.start <= point <= segment.end:
            return True
    return False
