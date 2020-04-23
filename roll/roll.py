#!/usr/bin/env python3

import argparse
import random
from printer import print_dices

parser = argparse.ArgumentParser(description='Dice Roller')

parser.add_argument('-n', '--launches',
                    dest='launches',
                    metavar='[0-9]+',
                    type=int, nargs=1, default=[1],
                    help='the number of dices to launch (default: 1)')

parser.add_argument('-b', '--bet',
                    dest='threshold',
                    metavar='[0-9]+',
                    type=int, nargs=1, default=[None],
                    help='if the sum of the dices is lower than this number the'
                        +' program will return a non-zero exit code')

parser.add_argument('-s', '--silent',
                    dest='silent',
                    action='store_true',
                    help='does not print the dices')

parser.add_argument('-t', '--total',
                    dest='print_sum',
                    action='store_true',
                    help='prints the sum of the dices')

args = parser.parse_args()
threshold = args.threshold[0] or 0
rolled_dices = [random.randint(1,6) for _ in range(args.launches[0])]
total = sum(rolled_dices)
not args.silent and print_dices(rolled_dices)
args.print_sum and print(total)
total < threshold and exit(threshold - total)
