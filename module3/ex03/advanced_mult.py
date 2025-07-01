#!/usr/bin/env python3

number = 0
while number <= 10:
    print(f"Table of {number}:", end=" ")
    
    mult = 0
    while mult <= 10:
        print(number * mult, end=" ")
        mult += 1

    print()
    number += 1