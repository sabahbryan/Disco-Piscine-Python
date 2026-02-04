#!/usr/bin/env python3

#import array

arr = [2, 8, 9, 48, 8, 22, -12, 2]

i = 0

print(arr)

while i < len(arr):
    arr[i] += 2
    print("A")
    if arr[i] <= 5:
        print("B")
        arr.pop(i)
    i += 1

print(arr)
