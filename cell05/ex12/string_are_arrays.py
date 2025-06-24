#!/usr/bin/env python3

import sys

if (len(sys.argv) - 1) != 1:
    print("none")
    sys.exit(1)

if 'z' not in sys.argv[1]:
    print("none")
    sys.exit(1)

for char in sys.argv[1]:
    if char == 'z':
        print('z', end = '')
print()

