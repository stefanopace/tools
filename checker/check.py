#!/usr/bin/env python3

import argparse
import sys

from subprocess import Popen, PIPE
from pyfzf.pyfzf import FzfPrompt

fzf = FzfPrompt()

parser = argparse.ArgumentParser(description='Dice Roller')

# parser.add_argument('-n', '--launches',
#                     dest='launches',
#                     metavar='[0-9]+',
#                     type=int, nargs=1, default=[1],
#                     help='the number of dices to launch (default: 1)')

parser.add_argument('-c', '--checklist',
                    dest='checklist',
                    metavar='<filepath>',
                    nargs=1,
                    help='')


# parser.add_argument('-s', '--silent',
#                     dest='silent',
#                     action='store_true',
#                     help='does not print the dices')
#
# parser.add_argument('-t', '--total',
#                     dest='print_sum',
#                     action='store_true',
#                     help='prints the sum of the dices')


def read_checklist_file(filename):
    with open(filename, 'r') as checklist_file:
        return checklist_file.read().splitlines()


def checked(label):
    return 'X ' + label


def unchecked(label):
    return label[2:]


def render_checklist(checklist):
    return [element["label"] for element in checklist]


def check_one(checklist):
    try:
        selected = fzf.prompt(render_checklist(checklist),
                              '--reverse --ansi --height 15 --border --header=checklist: --no-info'
                              )[0]
    except:
        exit(0)

    selected_prev_state = [element for element in checklist if element["label"] == selected]
    return checklist if not selected_prev_state else [
        element if not element["label"] == selected else {
            "checked": not element["checked"],
            "label": checked(element["label"]) if not selected_prev_state[0]["checked"] else unchecked(element["label"])
        } for element in checklist]


args = parser.parse_args()

elements = sys.stdin.read().splitlines() if not args.checklist[0] else read_checklist_file(args.checklist[0])
checklist = [{"checked": False, "label": element} for element in elements]
while True:
    checklist = check_one(checklist) or exit(0)
