"""
Base class that defines how base
features of a problem
"""

from __future__ import print_function, division
from utils.lib import *

class Decision(O):
  """
  Class depicting a decision for a problem
  """
  def __init__(self, name, low, high):
    O.__init__(self)
    self.name = name
    self.low = low
    self.high = high

  def norm(self, val):
    """
    Normalize Decision
    :param val:
    :return:
    """
    return norm(val, self.low, self.high)

  def de_norm(self, val):
    """
    De-normalize decision
    :param val:
    :return:
    """
    return de_norm(val, self.low, self.high)

class Objective(O):
  """
  Class depicting an objective for a problem
  """
  def __init__(self, name, to_minimize=True, low=None, high=None):
    O.__init__(self)
    self.name = name
    self.to_minimize = to_minimize
    self.low = low
    self.high = high
    self.value = None

  def norm(self, val):
    return norm(val, self.low, self.high)

class Constraint(O):
  """
  Class depicting constraint for a problem
  """
  def __init__(self, name):
    O.__init__(self)
    self.name = name
    self.value = None
    self.status = True


class Problem(O):
  def __init__(self):
    O.__init__(self)
    self.name = None
    self.decisions = None
    self.objectives = None
    self.constraints = None

  def generate(self, generator=uniform):
    """
    Generate a point based on a distribution
    :param generator:
    :return:
    """
    while True:
      one = [generator(d.low, d.high) for d in self.decisions]
      status = self.check_constraints(one)
      if status:
        return one

  def populate(self, n, generator = uniform):
    """
    Create a population of size n based on a generator function
    :param n:
    :param generator:
    :return:
    """
    population = []
    for _ in range(n):
      population.append(self.generate(generator))
    return population

  def norm_decisions(self, one):
    """
    Normalize decisions
    :param one: Set of decisions to be normalized
    :return: normalized decisions
    """
    nor = []
    for i, d in enumerate(self.decisions):
      nor.append(d.norm(one[i]))
    return nor

  def norm_objectives(self, one):
    """
    Normalize objectives
    :param one: Set of objectives to be normalized
    :return: normalized objectives
    """
    nor = []
    for i, o in enumerate(self.objectives):
      nor.append(o.norm(one[i]))
    return nor

  def check_constraints(self, decisions):
    """
    Check if a set of decisions satisfy
    the constraints
    :param one:
    :return:
    """
    return True

  def evaluate(self, decisions):
    """
    Evaluate a set of decisions
    :param decisions:
    :return:
    """
    return None
