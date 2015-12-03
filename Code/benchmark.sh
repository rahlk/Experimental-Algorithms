#!/usr/bin/env bash

if [ "$#" -ne 3 ]; then
  echo "Illegal number parameters"
  exit 1
fi


for (( N=1; N<=$1; N++ ))
  do
    echo "\nNumber of processors : $N"
    sh runner.sh $N $2 $3
done