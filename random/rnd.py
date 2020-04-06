#!/usr/bin/python3

import sys
import random

# defaults
char_amount = 10
use_numbers = True
num_from = '0'
num_to = '9'
use_lowercase = True
low_from = 'a'
low_to = 'z'
use_uppercase = True
upper_from = 'A'
upper_to = 'Z'


def char_range(c1, c2):
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)

args = sys.argv[1:]

if not all(argument.startswith('-') for argument in args):
    print ('arguments must starts with -')
    exit(1)

amount_arg = [int(arg[2:]) for arg in args if arg.startswith('-a')]
if amount_arg:
    char_amount = amount_arg[0]

number_arg = [[arg[2], arg[3]] for arg in args if arg.startswith('-n')]
if number_arg:
    num_from, num_to = number_arg[0]

lower_arg = [[arg[2], arg[3]] for arg in args if arg.startswith('-l')]
if lower_arg:
    low_from, low_to = lower_arg[0]

upper_arg = [[arg[2], arg[3]] for arg in args if arg.startswith('-u')]
if upper_arg:
    upper_from, upper_to = upper_arg[0]


char_pool = []
if use_numbers:
    char_pool += char_range(num_from, num_to)

if use_lowercase:
    char_pool += char_range(low_from, low_to)

if use_uppercase:
    char_pool += char_range(upper_from, upper_to)

for _ in range(char_amount):
    print(random.choice(char_pool), end='')

