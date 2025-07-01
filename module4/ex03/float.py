#!/usr/bin/env python3

user = (input("Give me a number: "))
try:
    val = int(user)
    print("This number is an integer")
except ValueError:
    val = float(user)
    print("This number is an float")