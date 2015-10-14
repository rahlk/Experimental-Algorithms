from __future__ import print_function, division
from problems.dtlz.dtlz2 import DTLZ2
from algorithms.serial.gale.gale import GALE as GALE_S
from algorithms.parallel.gale.gale import GALE as GALE_P
from algorithms.parallel.gale.gale import run as run_p
from mpi4py import MPI
from time import clock


COMM = MPI.COMM_WORLD
RANK = COMM.rank
SIZE = COMM.size

def _run_parallel():
  model = DTLZ2(3)
  gale = GALE_P(model)
  start = clock()
  goods = run_p(gale)
  if RANK == 0:
    delta = clock() - start
    print("Time taken ", delta)
    print(gale.convergence(goods))
    print(gale.diversity(goods))
    gale.solution_range(goods)

def _run_serial():
  model = DTLZ2(3)
  gale = GALE_S(model)
  start = clock()
  goods = gale.run()
  delta = clock() - start
  print("Time taken ", delta)
  print(gale.convergence(goods))
  print(gale.diversity(goods))
  gale.solution_range(goods)

if __name__ == "__main__":
  _run_serial()
