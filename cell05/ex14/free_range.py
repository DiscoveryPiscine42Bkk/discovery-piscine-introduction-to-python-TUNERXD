#!/usr/bin/env python3

import sys

if (len(sys.argv) - 1) != 2:
    print("none")
    sys.exit(1)

list = []
for i in range(int(sys.argv[1]), (int(sys.argv[2])) + 1):
    list.append(i)

print(list)