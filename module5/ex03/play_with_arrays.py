#!/usr/bin/env python3

#import array

arr1 = [2, 8, 9, 48, 8, 22, -12, 2, 3]
arr2 = arr1.copy()

i = 0

while i < len(arr2):
    arr2[i] += 2
    i += 1

i = 0

while i < len(arr2):
    if arr2[i] <= 5:
        arr2.pop(i)
        i = 0
    i += 1

i = 0

arr3 = set(arr2.copy())

print(arr1)
#print(arr2)
print(arr3)