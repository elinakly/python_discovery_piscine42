#!/usr/bin/env python3

import sys
import re

if len(sys.argv) < 2:
    print("none")
    exit()

for i in range(1, len(sys.argv)):
    if re.findall("ism", sys.argv[i]):
        continue
    else:
        sys.argv[i] += "ism"
print("\n".join(sys.argv[1:]))
