#!/usr/bin/env python3


def greetings(string = "noble stranger"):
    if isinstance(string, str):
        print(f"Hello, {string}.")
    else:
        print("Error! It was not a name.")

greetings('Alexandra')
greetings('wil')
greetings()
greetings(42)
