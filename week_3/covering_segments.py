# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    segments = sorted(segments)
    points = []

    current_reference_segment = segments[0]
    i = 1

    nb_segments = len(segments)
    while i < nb_segments:
        while i < nb_segments and current_reference_segment.start <= segments[i].start <= current_reference_segment.end:
            current_reference_segment_start = segments[i].start if current_reference_segment.start < segments[i].start else current_reference_segment.start
            current_reference_segment_end = segments[i].end if current_reference_segment.end > segments[i].end else current_reference_segment.end
            current_reference_segment = Segment(current_reference_segment_start, current_reference_segment_end)
            i += 1
        points.append(current_reference_segment.end)
        if i < nb_segments:
            current_reference_segment = segments[i]
            i += 1
    if current_reference_segment.end not in points:
        points.append(current_reference_segment.end)
    return points


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
