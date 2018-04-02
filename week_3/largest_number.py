# Uses python3

import sys


class LargestNumberKey:
    def __init__(self, number):
        self.number_str = number
        self.number = int(number)
        self.tens = len(number)

    def __lt__(self, other):
        return other.number * 10 ** self.tens + self.number > self.number * 10 ** other.tens + other.number

    def __gt__(self, other):
        return other.number * 10 ** self.tens + self.number < self.number * 10 ** other.tens + other.number

    def __eq__(self, other):
        return other.number * 10 ** self.tens + self.number == self.number * 10 ** other.tens + other.number

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return '{}, 10^{}'.format(self.number, self.tens)

    def __repr__(self):
        return '{}, 10^{}'.format(self.number, self.tens)


def largest_number(numbers):
    # write your code here
    keys = sorted([LargestNumberKey(number) for number in numbers], reverse=True)
    res = ''
    for key in keys:
        res += key.number_str
    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
