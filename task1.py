#бабл сорт
from random import randint

def bubbleSort(a):
    swap = True
    while swap == False:
        for i in range(len(a) - 1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                swap = True

a = [randint(1, 99) for i in range(10)]
print(a)
bubbleSort(a)
print(a)