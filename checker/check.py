#!/usr/bin/env python3

import sys

chosen = sys.argv[1].split(" ")
with open('stdup.txt') as txt:
    entries = [t.rstrip("\n") for t in txt.readlines()]
    for entry in entries:
        if entry in chosen:
            print(f'\033[7m{entry}\033[0m')
        else:
            print(f'{entry}')
