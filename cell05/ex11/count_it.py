#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:
    print("none")
    sys.exit(1)

print(f"parameters: {len(sys.argv)}")
for word in sys.argv[1:]:
    print(f"{word}: {len(word)}")

