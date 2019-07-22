#!/usr/bin/env bash

mkdir -p sandbox
cp ../archive sandbox
cd sandbox


echo 'Testing that one file is archived...'
touch test-file
./archive test-file

DATE=`date +%F`
ls -la .archive/$DATE | grep -e "^-.*test-file\$"
if [ "$?" != 0 ]; then
  echo -e "\e[31m failed to create current date directory \e[0m"
fi


cd ..
rm -rf sandbox
