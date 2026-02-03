#!/usr/bin/env python3

i = 0

num = int(input("Enter a number:\n"))
#ber = i * num

while i <= 9:
    ber = i * num
    print(f"{i} x {num} = {ber}")
    if i == 10:
        break
    i += 1
