#!/usr/bin/env python3

i = 0

while i <= 10:
    print(f"Table of {i}:", end = " ")
    j = 0
    while j <= 10:
        k = i * j
        print(f"{k}", end = " ")
        j += 1
    print()
    i += 1
