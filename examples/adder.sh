#!/usr/bin/env bash
cd '/home/alex/PycharmProjects/dis/examples'
for file in $(ls -la | grep "file$")
do
  echo 'DONT TRUST' >> file
done
