from __future__ import print_function, division
import sys, os
sys.path.append(os.path.abspath("."))
from problems.problem import *
from cocomo import Cocomo

__author__ = 'panzer'

class XOMO(Problem):
  """
  XOMO
  """
  def __init__(self):
    Problem.__init__(self)
    self.name = XOMO.__name__
    self.cocomo = Cocomo()
    self.names, lows, ups = [],[],[]
    for one in self.cocomo.about():
      self.names.append(one.txt)
      lows.append(one.min)
      ups.append(one.max)
    self.decisions = [Decision(self.names[i], lows[i], ups[i]) for i in range(len(self.names))]
    self.objectives = [Objective("effort", to_minimize=True, low = 0, high=43000),
                       Objective("months", to_minimize=True, low = 0, high=120),
                       Objective("defects", to_minimize=True, low = 0, high=1180000),
                       Objective("risk", to_minimize=True, low = 0, high=17)]

  @staticmethod
  def get_extremes():
    xomo = XOMO()
    mins = [sys.maxint]*4
    maxs = [-sys.maxint]*4
    for j in range(100000):
      print(j)
      x = xomo.cocomo.xys()
      for i, one in enumerate(x):
        if one < mins[i]: mins[i] = one
        if one > maxs[i]: maxs[i] = one
    print(mins)
    print(maxs)

  def evaluate(self, decisions):
    x = {}
    for n, d in zip(self.names, decisions): x[n] = int(round(d))
    return self.cocomo.xys(x)



