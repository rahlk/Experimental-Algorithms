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

  def limit(self, val):
    """
    Limit the value between
    low and high
    :param val:
    :return:
    """
    return max(self.low, min(val, self.high))

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

  def better(self, a, b):
    if self.to_minimize:
      return a < b
    else:
      return a > b

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

  def dist(self, one, two, one_norm = True, two_norm = True, is_obj = True):
    """
    Returns normalized euclidean distance between one and two
    :param one - Point A
    :param two - Point B
    :param one_norm - If A has to be normalized
    :param two_norm - If B has to be normalized
    :param is_obj - If the points are objectives or decisions
    """
    norm = self.norm_objectives if is_obj else self.norm_decisions
    one_norm = norm(one) if one_norm else one
    two_norm = norm(two) if two_norm else two
    delta = 0
    count = 0
    for i,j in zip(one_norm, two_norm):
      delta += (i-j) ** 2
      count += 1
    return (delta/count) ** 0.5

  def manhattan_dist(self, one, two, one_norm = True, two_norm = True, is_obj = True):
    """
    Returns manhattan distance between one and two
    :param one - Point A
    :param two - Point B
    :param one_norm - If A has to be normalized
    :param two_norm - If B has to be normalized
    :param is_obj - If the points are objectives or decisions
    """
    norm = self.norm_objectives if is_obj else self.norm_decisions
    one_norm = norm(one) if one_norm else one
    two_norm = norm(two) if two_norm else two
    delta = 0
    for i, j in zip(one_norm, two_norm):
      delta += abs(i -j)
    return delta

  def directional_weights(self):
    """
    Method that returns an array of weights
    based on the objective. If objective is
    to be maximized, return 1 else return 0
    :return:
    """
    weights = []
    for obj in self.objectives:
      # w is negative when we are maximizing that objective
      if obj.to_minimize:
        weights.append(1)
      else:
        weights.append(-1)
    return weights
