#!/usr/bin/env python3

num = int(input("Enter a number less than 25:\n"))

if num > 25:
    print("ERROR, can't you READ?!?!")

while num <= 25:
    print(f"Loop {num}")
    num += 1
