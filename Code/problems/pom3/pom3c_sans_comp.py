from __future__ import print_function, division
import sys, os
sys.path.append(os.path.abspath("."))
from problems.problem import *
from helper.pom3 import pom3

__author__ = 'panzer'

class POM3CSansComp(Problem):
  """
  POM 3C - without Completion
  """
  def __init__(self):
    Problem.__init__(self)
    self.name = POM3CSansComp.__name__
    names = ["Culture", "Criticality", "Criticality Modifier", "Initial Known", "Inter-Dependency", "Dynamism",
             "Size", "Plan", "Team Size"]
    lows = [0.50, 0.82, 2, 0.20, 0, 40, 2, 0, 20]
    ups = [0.90, 1.26, 8, 0.50, 50, 50, 4, 5, 44]
    self.decisions = [Decision(names[i], lows[i], ups[i]) for i in range(len(names))]
    self.objectives = [Objective("Cost", True, 0), Objective("Score", False, 0, 1),
                       Objective("Idle", True, 0, 1)]

  def evaluate(self, decisions):
    p = pom3()
    output = p.simulate(decisions)
    return [output[0], output[1], output[3]]


