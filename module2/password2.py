#!/usr/bin/env python3

code = "Python"

i = 1

while i > 0:
    word = input("Please input password: ")
    if word == code:
        print("GOOD")
        break
    print("ERROR")
    i += 1
