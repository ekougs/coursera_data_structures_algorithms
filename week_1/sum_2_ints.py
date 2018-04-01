# Uses python3
import sys

formatted_ints = sys.stdin.read()
tokens = formatted_ints.split()
a = int(tokens[0])
b = int(tokens[1])
print(a + b)
