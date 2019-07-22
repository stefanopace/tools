#!/usr/bin/env bash

TESTS=$(find -type f -name 'test*')
for TEST in $TESTS
do
  $(echo $TEST)
done
