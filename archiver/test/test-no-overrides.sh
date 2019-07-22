#!/usr/bin/env bash

mkdir -p sandbox
cp ../archive sandbox
cd sandbox


echo "Testing that don't overrides each others..."
echo "dont touch me!" > test-file
./archive test-file
echo "shakalaka!" > test-file
./archive test-file

DATE=`date +%F`
ls -la .archive/$DATE | grep -e "^-.*test-file.~1~\$"
if [ "$?" != 0 ]; then
  echo -e "\e[31m archiving files with same names don't rename archived file \e[0m"
fi

cat .archive/$DATE/test-file.~1~ | grep "dont touch me!"
if [ "$?" != 0 ]; then
  echo -e "\e[31m renamed files are not stored correctly \e[0m"
fi

cat .archive/$DATE/test-file | grep "shakalaka!"
if [ "$?" != 0 ]; then
  echo -e "\e[31m archiving files with same names overrides each others \e[0m"
fi


cd ..
rm -rf sandbox
