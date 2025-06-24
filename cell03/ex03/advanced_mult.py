#!/usr/bin/env python3
import sys

if len(sys.argv) != 1:
    print("none")
    sys.exit(1)


total_table = 10
total_num = 10
current_table = 0


while current_table <= total_table:

    current_num = 0
    print(f"Table de {current_table}: ", end = '')

    while current_num <= total_num:

        print(f"{current_table * current_num} ", end = '')
        current_num += 1

    current_table += 1 # increment to next table
    print()
