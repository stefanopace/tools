#!/usr/bin/env python3

import readline
import sys
from subprocess import check_output, run

if len(sys.argv) == 1:
    print('You must provide a filename to diff.')
    exit(code=1)

file_to_diff = sys.argv[1]

status_output = check_output(['svn', 'st']).decode('utf-8').split('\n')
modified_files = [line[8:] for line in status_output][0:-1]

matching_files = [file_path for file_path in modified_files if file_to_diff in file_path]

if len(matching_files) > 1:
    print('More than one file matches your input:')
    for matching_file in matching_files:
        print('- ' + matching_file)
    print('Be more precise...')
else:
    run(['svn', 'diff', matching_files[0]])
