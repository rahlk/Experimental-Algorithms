"""
DTLZ2 is a mathematical test problem which was formulated by
Kalyanmoy Deb, Lothar Thiele, Marco Laumans and Eckhart Zitzler.
Our version of DTLZ2 has 3 objectives. The ideal pareto
frontier lies on the first octant of radius 1
"""
from __future__ import print_function, division
import sys, os
sys.path.append(os.path.abspath("."))
from problems.problem import *
from utils.lib import *

class DTLZ2(Problem):
  """
  Hypothetical test problem with
  "m" objectives and "n" decisions
  """
  k = 10
  def __init__(self, m, n=None):
    Problem.__init__(self)
    self.name = DTLZ2.__name__
    if n is None:
      n = DTLZ2.default_decision_count(m)
    self.decisions = [Decision("x"+str(i+1), 0, 1) for i in range(n)]
    self.objectives = [Objective("f"+str(index+1), True, 0, 1000) for index in range(m)]

  @staticmethod
  def default_decision_count(m):
    return m + DTLZ2.k - 1

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

  def get_ideal_objectives(self):
    rows = []
    with open("problems/dtlz/DTLZ2_3D.csv", "r") as f:
      lines = f.readlines()
      for line in lines:
        rows.append([float(pt) for pt in line.split(",")])
    return rows