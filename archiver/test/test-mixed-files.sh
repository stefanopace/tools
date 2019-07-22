#!/usr/bin/env bash

mkdir -p sandbox
cp ../archive sandbox
cd sandbox


echo 'Testing that one file is archived...'
touch test-file1
touch test-file2
mkdir test-dir
touch test-dir/test-file3
touch test-dir/test-file4
./archive test-file1 test-dir test-file2

DATE=`date +%F`
ls -la .archive/$DATE | grep -e "^-.*test-file1\$"
if [ "$?" != 0 ]; then
  echo -e "\e[31m failed to create first file on mixed file archive \e[0m"
fi

ls -la .archive/$DATE | grep -e "^d.*test-dir\$"
if [ "$?" != 0 ]; then
  echo -e "\e[31m failed to create archived directory on mixed file archive \e[0m"
fi

ls -la .archive/$DATE/test-dir | grep -e "^-.*test-file3\$"
if [ "$?" != 0 ]; then
  echo -e "\e[31m directory are not archived recursively on mixed file archive \e[0m"
fi
ls -la .archive/$DATE/test-dir | grep -e "^-.*test-file4\$"
if [ "$?" != 0 ]; then
  echo -e "\e[31m directory are not archived recursively for all files on mixed file archive \e[0m"
fi

ls -la .archive/$DATE | grep -e "^-.*test-file2\$"
if [ "$?" != 0 ]; then
  echo -e "\e[31m failed to create second file on multiple file archive on mixed file archive \e[0m"
fi


cd ..
rm -rf sandbox
