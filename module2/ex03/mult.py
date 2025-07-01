#!/usr/bin/env python3

first = int(input("Enter the first number:\n"))
second = int(input("Enter the second number:\n"))

result = first * second
print(first, "x", second, "=", result, sep=" ")
if result == 0:
    print("This number is both positive and negative.")
elif result < 0:
    print("This number is negative.")
else:
    print("This number is positive.")