#!/usr/bin/env python3

try:
    number = int(input("")).strip()

    if number > 0:
        print("This number is positive.")
    elif number < 0:
        print("This number is negative.")
    else:
        print("This number is both positive and negative.")
except ValueError:
    print("Not a number.")