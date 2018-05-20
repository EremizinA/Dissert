#!/usr/bin/env bash
cd '/home/alex/PycharmProjects/dis/examples/dirs'
for file in $(ls)
do
  rm ${file}
done