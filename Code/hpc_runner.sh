#! /bin/tcsh

if [ "$#" -ne 2 ]; then
  echo "Illegal number parameters"
  echo "sh hpc_runner.sh <number of processors> <optimizer>"
  exit 1
fi

bsub -W 6000 -n $1 -o out/$2_$1.out.%J -e err/$2_$1.err.%J sh runner.sh $1 $2 > log/$2_$1.log