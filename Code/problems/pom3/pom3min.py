from __future__ import print_function, division
import sys, os
sys.path.append(os.path.abspath("."))
from problems.problem import *
from helper.pom3 import pom3

__author__ = 'panzer'

class POM3Min(Problem):
  """
  POM 3 Min
  """
  def __init__(self):
    Problem.__init__(self)
    self.name = POM3Min.__name__
    names = ["Culture", "Criticality", "Criticality Modifier", "Initial Known", "Inter-Dependency", "Dynamism",
             "Size", "Plan", "Team Size"]
    lows = [0.80, 1.22, 2, 0.60, 0, 1, 0, 0, 1]
    ups = [0.90, 1.62, 6, 0.62, 2, 3, 1, 1, 3]
    self.decisions = [Decision(names[i], lows[i], ups[i]) for i in range(len(names))]
    self.objectives = [Objective("Cost", True), Objective("Score", False),
                       Objective("Completion", False), Objective("Idle", True)]

  def evaluate(self, decisions):
    p = pom3()
    return p.simulate(decisions)

