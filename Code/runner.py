from __future__ import print_function, division
from problems.dtlz.dtlz2 import DTLZ2
#from algorithms.serial.gale.gale import GALE
from algorithms.parallel.gale.gale import GALE
from mpi4py import MPI

COMM = MPI.COMM_WORLD
RANK = COMM.rank
SIZE = COMM.size

def _run_parallel():
  model = DTLZ2(3)
  gale = GALE(model)
  goods = gale.run()
  if RANK == 0:
    print(gale.convergence(goods))
    print(gale.diversity(goods))
    gale.solution_range(goods)

def _run_serial():
  model = DTLZ2(3)
  gale = GALE(model)
  goods = gale.run()
  print(gale.convergence(goods))
  print(gale.diversity(goods))
  gale.solution_range(goods)

if __name__ == "__main__":
  _run_serial()
