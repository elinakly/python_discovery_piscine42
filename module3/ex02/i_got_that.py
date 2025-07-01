#!/usr/bin/env python3

password = "STOP"

string = input("What you gotta say? : ")
if string == password:
    exit()
while input("I got that! Anything else? : ") != password:
    continue