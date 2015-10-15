from __future__ import print_function, division
from problems.dtlz.dtlz2 import DTLZ2
from algorithms.serial.gale.gale import GALE as GALE_S
from algorithms.parallel.gale.gale import GALE as GALE_P
from algorithms.parallel.gale.gale import run as run_p
from algorithms.serial.de.de import DE as DE_S
from mpi4py import MPI
from time import clock, sleep
from utils.lib import O, report


COMM = MPI.COMM_WORLD
RANK = COMM.rank
SIZE = COMM.size

settings = O(
  runs = 20
)

def _run_parallel():
  model = DTLZ2(3)
  gale = GALE_P(model)
  times, convs, dives = [], [], []
  for i in range(settings.runs):
    print(i)
    start = clock()
    goods = run_p(gale, id = i)
    if RANK == 0:
      times.append(clock() - start)
      convs.append(gale.convergence(goods))
      dives.append(gale.diversity(goods))
  if RANK == 0:
    report(times, "Time Taken")
    report(convs, "Convergence")
    report(dives, "Diversity")



def _run_serial():
  times, convs, dives = [], [], []
  for i in range(settings.runs):
    model = DTLZ2(3)
    gale = GALE_S(model)
    start = clock()
    print(i)
    goods = gale.run()
    times.append(clock() - start)
    convs.append(gale.convergence(goods))
    dives.append(gale.diversity(goods))
    gale.solution_range(goods)
  report(times, "Time Taken")
  report(convs, "Convergence")
  report(dives, "Diversity")

def _run_once():
  model = DTLZ2(3)
  de = DE_S(model)
  start = clock()
  goods = de.run()
  delta = clock() - start
  print("Time taken ", delta)
  print(de.convergence(goods))
  print(de.diversity(goods))
  de.solution_range(goods)

if __name__ == "__main__":
  _run_once()
