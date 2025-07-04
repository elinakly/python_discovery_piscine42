#!/usr/bin/env python3

import sys

if (len(sys.argv) < 2):
    print("none")
    exit()
print (f"parameters: {len(sys.argv) - 1}")
for i in range(1, len(sys.argv)):
    print(f"{sys.argv[i]}: {len(sys.argv[i])}")
