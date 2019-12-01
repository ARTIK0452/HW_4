import random
from random import randint

def quickSort(a):
    if len(a) <= 1:
        return a
    else:
        b = random.choice(a)
        left_min_b = [elem for elem in a if elem < b]
        M = [b] * a.count(b)
        right_max_b = [elem for elem in a if elem > b]
        return quickSort(left_min_b) + M + quickSort(right_max_b)
a = [randint(1, 99) for i in range(10)]
print(a)
print(quickSort(a))