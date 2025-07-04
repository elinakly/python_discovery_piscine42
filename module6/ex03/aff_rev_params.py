#!/usr/bin/env python3

import sys

if (len(sys.argv) == 1):
    print("none")
    exit()

for i in reversed(range(1, len(sys.argv))):
    print(f"{sys.argv[i]}") 
