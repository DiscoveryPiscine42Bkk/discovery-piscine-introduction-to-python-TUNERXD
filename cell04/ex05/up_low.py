#!/usr/bin/env python3

usr_inp = input("")
new = ""

for char in usr_inp:
    if char.isupper():
        new += char.lower()
    elif char.islower():
        new += char.upper()
    else:
        new += char

print(new)