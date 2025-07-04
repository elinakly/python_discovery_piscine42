#!/usr/bin/env python3

import sys

if (len(sys.argv) != 2):
    print("none")
    exit()
param = sys.argv[1]
if input("What was the parameter? ") != param:
    print("Nope, sorry.")
else:
    print("Good job!")