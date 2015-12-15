#! /bin/tcsh

if [ "$#" -ne 3 ]; then
  echo "Illegal number parameters"
  echo "sh hpc_runner.sh <number of processors> <optimizer> <model>"
  exit 1
fi

bsub -W 600 -n $1 -o out/$2_$3_$1.out.%J -e err/$2_$3_$1.err.%J sh runner.sh $1 $2 $3 > log/$2_$3_$1.log