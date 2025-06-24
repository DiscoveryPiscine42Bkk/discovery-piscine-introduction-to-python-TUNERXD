#!/usr/bin/env python3

try:
    num = int(input("Enter a number \n").strip())

    for i in range(10):
        result =  num * i
        print(f"{i} x {num} = {result}")


except ValueError:
    print("Not a number")