#!/usr/bin/env bash

mkdir -p sandbox
cp ../archive sandbox
cd sandbox


echo 'Testing that the directories are created...'
touch test-file
./archive test-file

ls -la . | grep -e "^d.*\.archive\$"
if [ "$?" != 0 ]; then
  echo -e "\e[31m failed to create .archive directory \e[0m"
fi

DATE=`date +%F`
ls -la .archive | grep -e "^d.*$DATE\$"
if [ "$?" != 0 ]; then
  echo -e "\e[31m failed to create current date directory \e[0m"
fi


cd ..
rm -rf sandbox
