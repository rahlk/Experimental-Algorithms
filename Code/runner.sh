#!/usr/bin/env bash

if [ "$#" -ne 3 ]; then
  echo "Illegal number parameters"
  exit 1
fi

mpiexec -n $1 $PYTHON runner.py $2 $3