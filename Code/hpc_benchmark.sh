#! /bin/tcsh

if [ "$#" -ne 2 ]; then
  echo "Illegal number parameters"
  echo "sh hpc_benchmark.sh <number of processors> <optimizer>"
  exit 1
fi

bsub -W 6000 -n $1 -o out/bm_$2_$1.out.%J -e err/bm_$2_$1.err.%J sh benchmark.sh $1 $2 > log/bm_$2_$1.log