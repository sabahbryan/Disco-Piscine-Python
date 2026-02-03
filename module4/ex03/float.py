#!/usr/bin/env python3

num = input("Please input a number: ")
dec = num.isdigit()

if dec == True:
    print("This number is an integer.")
else:
    print("This number is a decimal(float).")
