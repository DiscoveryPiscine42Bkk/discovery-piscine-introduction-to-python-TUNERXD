#!/usr/bin/env python3
import sys


def main():

    if len(sys.argv) > 1:
        print("none")
        sys.exit(1)


    total_table = 10
    total_num = 10
    current_table = 0
    current_num = 0

    while current_table <= total_table:
        print(f"Table de {current_table}: ", end = '')
        while current_num <= total_num:
            result = current_table * current_num
            print(f"{result} ", end = '')
            current_num += 1
        current_num = 0 # reset current_num to 0
        current_table += 1 # increment to next table
        print()

if __name__ == "__main__":
    main()