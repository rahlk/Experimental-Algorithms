from __future__ import print_function, division
from problems.dtlz2 import DTLZ2
from algorithms.parallel.gale.gale import GALE, run

if __name__ == "__main__":
  model = DTLZ2()
  gale = GALE(model)
  run(gale)
  #print(gale.convergence(goods))
  #print(gale.diversity(goods))
  #gale.solution_range(goods)

