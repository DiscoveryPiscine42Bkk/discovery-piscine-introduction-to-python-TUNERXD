#!/usr/bin/env python3
import sys


def main():
    
    if len(sys.argv) < 2:
        print("none")
        sys.exit(1)
    
    for arg in sys.argv[1:]:
        print(downcase_all(arg))



def downcase_all(s):
    return s.lower()


if __name__ == "__main__":
    main()
