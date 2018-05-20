#!/usr/bin/env bash
cd '/home/alex/PycharmProjects/dis/examples'
mkdir dirs
cd dirs
i=0
while [ ${i} -le 5 ]
do
  touch file${i}
  i=$((i+1))
done