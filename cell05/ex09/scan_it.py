#!/usr/bin/env python3

import re
import sys

param_len = len(sys.argv)

if param_len != 3:
    print("none")
    sys.exit(1)

key = sys.argv[1]
string = sys.argv[2]

match = re.findall(key , string)
print(len(match))
