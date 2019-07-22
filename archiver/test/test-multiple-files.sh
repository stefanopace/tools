#!/usr/bin/env bash

mkdir -p sandbox
cp ../archive sandbox
cd sandbox


echo 'Testing that one file is archived...'
touch test-file1
touch test-file2
touch test-file3
./archive test-file1 test-file2 test-file3

DATE=`date +%F`
ls -la .archive/$DATE | grep -e "^-.*test-file1\$"
if [ "$?" != 0 ]; then
  echo -e "\e[31m failed to create first file on multiple file archive \e[0m"
fi
ls -la .archive/$DATE | grep -e "^-.*test-file2\$"
if [ "$?" != 0 ]; then
  echo -e "\e[31m failed to create second file on multiple file archive \e[0m"
fi
ls -la .archive/$DATE | grep -e "^-.*test-file3\$"
if [ "$?" != 0 ]; then
  echo -e "\e[31m failed to create third file on multiple file archive \e[0m"
fi


cd ..
rm -rf sandbox
