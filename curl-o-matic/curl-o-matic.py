#!/usr/bin/env python3

import sys
import fixer
import tester

if len(sys.argv) > 1 and sys.argv[1] == 'fix':
    print('Saving curl responses...')
    fixer.store_responses()
    print('Done')
else:
    tester.check_same()
