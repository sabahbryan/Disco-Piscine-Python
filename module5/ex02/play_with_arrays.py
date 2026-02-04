#!/usr/bin/env python3

#import array

arr = [2, 8, 9, 48, 8, 22, -12, 2]

arr2 = arr.copy()

i = 0

print(arr)

while i < len(arr):
    arr[i] += 2
#    print("A")
#    if arr[i] <= 5:
#        arr.pop(i)
    i += 1

print(arr)

i = 0

while i < len(arr):
#    print("B")
    if arr[i] <= 5:
#        print("C")
        arr.pop(i)
        i = 0
    i += 1

print(arr)
