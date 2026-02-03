#!/usr/bin/env python3

i = 1

print("What you gotta say? : ")

while i > 0:
    text = input()
    if text == "STOP":
        break
    print(f"I got that! Anything else? : {text}")
    i += 1
