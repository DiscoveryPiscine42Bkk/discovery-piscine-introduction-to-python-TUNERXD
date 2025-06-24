#!/usr/bin/env python3

try:
    print("Enter a number")
    num = int(input("").strip())

    for i in range(10):
        result =  num * i
        print(f"{i} x {num} = {result}")


except ValueError:
    print("Not a number")