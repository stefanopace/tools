#!/usr/bin/env python3

# add this to .bashrc to run todo -s after cd command
#
# [ -z "$PS1" ] && return
#
# function cd {
#     builtin cd "$@" && todo -s && return
#     }

import argparse
from todo_item import TodoItem
from os import remove

parser = argparse.ArgumentParser(description='Manage a todo list.')

parser.add_argument('new_item',
                    metavar='something',
                    type=str, nargs='*',
                    help='a new entry in the todo list')

parser.add_argument('-d', '--done',
                    dest='done_item',
                    metavar='something',
                    type=str, nargs='+',
                    help='an entry to be marked as done')

parser.add_argument('-u', '--undone',
                    dest='undone_item',
                    metavar='something',
                    type=str, nargs='+',
                    help='an entry to be marked as todo')

parser.add_argument('-r', '--remove',
                    dest='removed_item',
                    metavar='something',
                    type=str, nargs='+',
                    help='an entry to be removed from the list')

parser.add_argument('-a', '--all',
                    dest='all',
                    action='store_true',
                    help='apply changes to all matches, if used without other arguments show also done items')

parser.add_argument('-s', '--silent',
                    dest='silent',
                    action='store_true',
                    help='don\'t output anything if there is nothing to do')

args = parser.parse_args()


mutual_exclusion_options = [args.new_item, args.done_item, args.undone_item, args.removed_item]
args_count = len([option for option in mutual_exclusion_options if option is not None and option])
if args_count > 1:
    print('Sorry, only one operation at time is supported')
    exit(1)

filename = './.todo'


def read_todo_list():
    try:
        with open(filename, 'r') as todo_file:
            todo_list = todo_file.readlines()
    except FileNotFoundError:
        return []
    except EnvironmentError as err:
        print(str(err))
    else:
        try:
            return [TodoItem.deserialize(item) for item in todo_list]
        except ValueError:
            print('Your .todo file seems to be broken. Check it for syntax errors.')
            exit(1)


def no_arguments_are_passed():
    return not args.new_item and \
           not args.done_item and \
           not args.removed_item and \
           not args.undone_item


def show_todo_list(todo_list):
    if not [item for item in todo_list if item.status == 'todo'] and not args.all:
        if not args.silent:
            print('Nothing to do here...\n'
                  'type \'todo something\' to add a todo or\n'
                  'type \'todo -a\' to show done items or\n'
                  'type \'todo -h\' for usage info.')
    else:
        print('There is something to do here:')
        for item in todo_list:
            if item.status == 'todo' or args.all:
                print('\t' + str(item))


if no_arguments_are_passed():
    todo_list = read_todo_list()
    if not todo_list:
        if not args.silent:
            print('Nothing to do here...\n'
                  'type \'todo something\' to add a todo or\n'
                  'type \'todo -h\' for usage info.')
    else:
        show_todo_list(todo_list)

if args.new_item:
    new_content = ' '.join(args.new_item)
    new_item = TodoItem(new_content)
    todo_list = read_todo_list()
    not_done_items = [item for item in todo_list if item.status == 'todo']
    for item in not_done_items:
        if item.content == new_item.content:
            print('This item already exists:\n' +
                  '\t' + str(item))
            exit(0)
    try:
        with open(filename, 'a') as todo_file:
            todo_file.write(new_item.serialize() + '\n')
    except EnvironmentError as err:
        print(str(err))
    else:
        print('You have one more thing to do: \n' + '\t' + str(new_item))

if args.done_item:
    done_content = ' '.join(args.done_item)
    todo_list = read_todo_list()
    not_done_items = [item for item in todo_list if item.status == 'todo']
    matches = [item for item in not_done_items if done_content in item.content]
    if not matches:
        print('Nothing matches what have you done, check your spelling or type \'todo\' to check the list')
    elif len(matches) > 1 and not args.all:
        print('More than one items matches what have you done, be more precise or '
              'use -a option to mark all matches as done')
        print('Matches for \'' + done_content + '\':')
        [print('\t' + str(match)) for match in matches]
    else:
        for item in matches:
            item.done()
        try:
            with open(filename, 'w') as todo_file:
                for item in todo_list:
                    todo_file.write(item.serialize() + '\n')
        except EnvironmentError as err:
            print(str(err))
        else:
            print('You have done this:')
            for match in matches:
                print('\t' + str(match))

if args.undone_item:
    undone_content = ' '.join(args.undone_item)
    todo_list = read_todo_list()
    not_todo_items = [item for item in todo_list if item.status == 'done']
    matches = [item for item in not_todo_items if undone_content in item.content]
    if not matches:
        print('Nothing matches what have you want to undone, check your spelling or type \'todo -a\' to check '
              'the list with done items')
    elif len(matches) > 1 and not args.all:
        print('More than one items matches what have you done, be more precise or '
              'use -a option to mark all matches as done')
        print('Matches for \'' + undone_content + '\':')
        [print('\t' + str(match)) for match in matches]
    else:
        for item in matches:
            item.undone()
        try:
            with open(filename, 'w') as todo_file:
                for item in todo_list:
                    todo_file.write(item.serialize() + '\n')
        except EnvironmentError as err:
            print(str(err))
        else:
            print('You have to do this again:')
            for match in matches:
                print('\t' + str(match))

if args.removed_item:
    removed_content = ' '.join(args.removed_item)
    todo_list = read_todo_list()
    matches = [item for item in todo_list if removed_content in item.content]
    if not matches:
        print('Nothing matches what you want to remove, check your spelling or type \'todo -a\' to check '
              'the list with done items')
    elif len(matches) > 1 and not args.all:
        print('More than one items matches what you want to remove, be more precise or '
              'use -a option to remove all matches')
        print('Matches for \'' + removed_content + '\':')
        [print('\t' + str(match)) for match in matches]
    else:
        for item in matches:
            todo_list.remove(item)
        if not todo_list:
            print('You have permanently removed these items:')
            for match in matches:
                print('\t' + str(match))
            print('Your todo list is empty, i will remove the .todo file')
            try:
                remove(filename)
            except OSError:
                print('I was unable to remove the file, you may have to delete it manually')
        else:
            try:
                with open(filename, 'w') as todo_file:
                    for item in todo_list:
                        todo_file.write(item.serialize() + '\n')
            except EnvironmentError as err:
                print(str(err))
            else:
                print('You have permanently removed these items:')
                for match in matches:
                    print('\t' + str(match))
