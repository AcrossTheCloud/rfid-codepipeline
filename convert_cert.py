#!/usr/bin/env python3

import sys

with open(sys.argv[1],'r') as file:
    for line in file:
        if "END" not in line:
            print(line.rstrip()+'\\n\\')
        else:
            print(line.rstrip()+'\\n')
