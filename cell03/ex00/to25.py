#!/usr/bin/env python3

try:
    num = int(input("Enter a number less than 25 \n").strip())

    if num > 25:
        raise ValueError
    
    while num <= 25:
        print(f"Inside the loop, my variable is {num}")
        num += 1

except ValueError:
    print("Error")

