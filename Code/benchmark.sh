#!/usr/bin/env bash

if [ "$#" -ne 2 ]; then
  echo "Illegal number parameters"
  exit 1
fi


for (( N=2; N<=$1; N++ ))
  do
    echo "\nNumber of processors : $N"
    sh runner.sh $N $2
done