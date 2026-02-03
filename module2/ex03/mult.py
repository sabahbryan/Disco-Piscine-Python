#!/usr/bin/env python3

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

num = a * b

if num > 0:
    print(f"By the powers combined, the result is {num}!\n...Hence a POSITIVE!")
elif num < 0:
    print(f"By the powers combined, the result is {num}!\n...Hence a NEGATIVE!")
else:
    print(f"By the powers combined, the result is {num}!\n...Hence it's BOTH?!?!")
