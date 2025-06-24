#!/usr/bin/env python3
import sys

len = len(sys.argv)

if len < 2:
    print("none")
    sys.exit(1)

for i in range(len - 1):
    print(sys.argv[len - i - 1])