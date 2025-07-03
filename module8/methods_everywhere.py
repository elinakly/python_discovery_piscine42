#!/usr/bin/env python3

import sys

def shrink(string):
    print(string[0:8])


def enlarge(string):
    while (len(string) != 8):
        string += 'z'
    print(string)

if (len(sys.argv) < 2):
    print("none")
    exit()

for i in range(1, len(sys.argv)):
    if (len(sys.argv[i])) < 8:
        enlarge(sys.argv[i])
    else:
        shrink(sys.argv[i])