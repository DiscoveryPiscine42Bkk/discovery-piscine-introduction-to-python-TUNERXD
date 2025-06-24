#!/usr/bin/env python3

import re
import sys

param_len = len(sys.argv)

if param_len != 2:
    print("none")
    sys.exit(1)

param = sys.argv[1]
usr_inp = input("What was the parameter? ")

if param == usr_inp:
    print("Good job!")
else:
    print("Nope, sorry...")
