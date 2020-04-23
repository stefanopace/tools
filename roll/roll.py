#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description='Dice Roller')

parser.add_argument('-n', '--launches',
                    dest='launches',
                    metavar='[0-9]+',
                    type=int, nargs=1, default=1,
                    help='the number of dice to launch (default: 1)')

parser.add_argument('-t', '--threshold',
                    dest='threshold',
                    metavar='[0-9]+',
                    type=int, nargs=1,
                    help='if the sum of the dice is lower than this number the program will return a non-zero exit code')

parser.add_argument('-s', '--silent',
                    dest='silent',
                    action='store_true',
                    help='does not print the output')

parser.add_argument('-s', '--silent',
                    dest='silent',
                    action='store_true',
                    help='don\'t output anything if there is nothing to do')

args = parser.parse_args()

print(args)
