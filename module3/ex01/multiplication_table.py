#!/usr/bin/env python3

number = int(input("Enter a number\n"))
mult = 0
while mult <= 9:
    result = number * mult
    print(f"{mult} x {number} = {result}")
    mult += 1
