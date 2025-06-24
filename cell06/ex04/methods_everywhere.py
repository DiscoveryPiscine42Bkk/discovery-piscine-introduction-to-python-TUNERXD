#!/usr/bin/env python3
import sys


def main():
    
    if len(sys.argv) < 2:
        print("none")
        sys.exit(1)
    
    for arg in sys.argv[1:]:
        if len(arg) > 8:
            print(shrink(arg))
        elif len(arg) < 8:
            print(enlarge(arg))
        else:
            print(arg)


def shrink(s):
    return s[:8]


def enlarge(s):

    i = 8 - len(s)
    return s + ('Z' * i)


if __name__ == "__main__":
    main()
