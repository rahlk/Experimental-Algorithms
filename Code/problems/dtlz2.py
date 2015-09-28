"""
DTLZ2 is a mathematical test problem which was formulated by
Kalyanmoy Deb, Lothar Thiele, Marco Laumans and Eckhart Zitzler.
Our version of DTLZ2 has 30 decisions between 0 and 1 and
3 objectives. The ideal pareto frontier lies on the first octant
of radius 1
"""
from __future__ import print_function, division
from problem import *
from utils.lib import *

class DTLZ2(Problem):
  def __init__(self):
    Problem.__init__(self)
    self.name = "DTLZ2"
    self.decisions = [Decision("x"+str(i+1), 0, 1) for i in range(30)]
    self.objectives = [
      Objective("f1", True, 0, 1),
      Objective("f2", True, 0, 1),
      Objective("f3", True, 0, 1)
    ]

  def evaluate(self, decisions):
    n_decs = len(self.decisions)
    n_objs = len(self.objectives)
    k = n_decs - n_objs + 1
    g =  sum([(decisions[i] - 0.5)**2 for i in range(n_decs-k, n_decs)])
    objs = [1 + g] * n_objs
    for i in range(n_objs):
      for j in range(n_objs - i - 1):
        objs[i] *= cos(0.5 * PI * decisions[j])
      if i != 0:
        objs[i] *= sin(0.5 * PI * decisions[n_objs - i - 1])
    return objs

