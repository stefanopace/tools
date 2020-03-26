#!/usr/bin/env bash
port=7116

for ip in $(hostname -I)
do
  echo "http://$ip:$port/"
done

python3 -m http.server $port
