#!/usr/bin/env python3

import sys

def downcase_all(string):
    return(string.lower())


if (len(sys.argv) < 2):
    print("none")
    exit()

for i in sys.argv:
    print(downcase_all(i))