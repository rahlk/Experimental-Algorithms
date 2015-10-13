from __future__ import print_function, division
from problems.dtlz.dtlz2 import DTLZ2
from algorithms.serial.gale.gale import GALE

if __name__ == "__main__":
  model = DTLZ2(3)
  model.get_pareto_front()
  # gale = GALE(model)
  # goods = gale.run()
  # #print(gale.convergence(goods))
  # #print(gale.diversity(goods))
  # gale.solution_range(goods)

