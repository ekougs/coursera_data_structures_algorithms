# Uses python3
nb_ints = int(input())
ints = [int(x) for x in input().split()]

greatest_int = None
scnd_greatest_int = None

for i in ints:
    if greatest_int is None or i > greatest_int:
        scnd_greatest_int = greatest_int
        greatest_int = i
    elif scnd_greatest_int is None or i > scnd_greatest_int:
        scnd_greatest_int = i

print(greatest_int * scnd_greatest_int)
