#!/usr/bin/env python3

import sys
import re

if (len(sys.argv) != 2):
    print("none")
    exit()
number = len(re.findall('z', sys.argv[1]))
string = "".join(re.findall('z', sys.argv[1]))
if number == 0:
    print("none")
else:
    print(f"{string}")
