#!/usr/bin/env bash

mkdir -p sandbox
cp ../archive sandbox
cd sandbox


echo "Testing that directory don't overrides each others..."
mkdir test-dir
touch test-dir/test-file1
touch test-dir/test-file2
./archive test-dir
mkdir test-dir
touch test-dir/test-file3
touch test-dir/test-file4
./archive test-dir

DATE=`date +%F`
ls -la .archive/$DATE | grep -e "^d.*test-dir\$"
if [ "$?" != 0 ]; then
  echo -e "\e[31m failed to create archived directory \e[0m"
fi

ls -la .archive/$DATE/test-dir | grep -e "^-.*test-file3\$"
if [ "$?" != 0 ]; then
  echo -e "\e[31m directory are not archived recursively \e[0m"
fi
ls -la .archive/$DATE/test-dir | grep -e "^-.*test-file4\$"
if [ "$?" != 0 ]; then
  echo -e "\e[31m directory are not archived recursively for all files \e[0m"
fi

ls -la .archive/$DATE | grep -e "^d.*test-dir.~1~\$"
if [ "$?" != 0 ]; then
  echo -e "\e[31m failed to create archived directory \e[0m"
fi

ls -la .archive/$DATE/test-dir.~1~ | grep -e "^-.*test-file1\$"
if [ "$?" != 0 ]; then
  echo -e "\e[31m directory are not archived recursively \e[0m"
fi
ls -la .archive/$DATE/test-dir.~1~ | grep -e "^-.*test-file2\$"
if [ "$?" != 0 ]; then
  echo -e "\e[31m directory are not archived recursively for all files \e[0m"
fi

cd ..
rm -rf sandbox
