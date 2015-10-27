from __future__ import print_function, division
import sys, os
sys.path.append(os.path.abspath("."))
from mpi4py import MPI
from utils.lib import *
from algorithms.serial.algorithm import Algorithm

COMM = MPI.COMM_WORLD

RANK = COMM.rank
SIZE = COMM.size

def default_settings():
  """
  Default Settings for DE
  :return: default settings
  """
  return O(
    gens = 100,
    candidates = 160,
    f = 0.75,
    cr = 0.3,
    seed = 1
  )

def per_core(value):
  return int(round(value/SIZE))

class DE(Algorithm):
  """
  Differential Evolution
  Storn 97
  """
  def __init__(self, problem, **settings):
    """
    Initialize DE for Algorithm
    """
    Algorithm.__init__(self, DE.__name__, problem)
    self.settings = default_settings().update(**settings)

  def dominates(self, obj1, obj2):
    """
    Static method to check if one objective
    dominate the other.
    :param obj1: List of points A
    :param obj2: List of points B
    """
    at_least = False
    for i,(a, b) in enumerate(zip(obj1, obj2)):
      if self.problem.objectives[i].better(a,b):
        at_least = True
      elif a == b:
        continue
      else:
        return False
    return at_least

  @staticmethod
  def three_others(one, pop):
    """
    Return three other points from population
    :param one: Point not to consider
    :param pop: Population to look in
    :return: two, three, four
    """
    def one_other():
      while True:
        x = choice(pop)
        if not id(x) in seen:
          seen.append(id(x))
          return x
    seen = [id(one)]
    two = one_other()
    three = one_other()
    four = one_other()
    return two, three, four

  def mutate(self, one, pop):
    """
    Function to mutate point using
    DE mutation strategy and return it
    :param one: Point to be mutated
    :param pop: Population to mutate from
    :return: Mutated point
    """
    two, three, four = DE.three_others(one, pop)
    r = choice(range(len(one.decisions)))
    mutated_decs = one.decisions[:]
    for i in range(len(one.decisions)):
      if (rand() < self.settings.cr) or (r == i):
        mutated_decs[i] = self.problem.decisions[i].limit(
          two.decisions[i] + self.settings.f * (three.decisions[i] - four.decisions[i]))
    return Point(mutated_decs)

  def generate(self, size):
    """
    Generate the population
    :return:
    """
    pop = self.problem.populate(size)
    return [Point(one) for one in pop]

  @staticmethod
  def run(algo, id = 0):
    """
    Run DE
    :param pop:
    :return:
    """
    gen = 0
    size = per_core(algo.settings.candidates)
    max_gens = algo.settings.gens
    pop = algo.generate(size)
    for one in pop: one.evaluate(algo.problem)
    while gen < max_gens:
      say(".")
      clones = [one.clone() for one in pop]
      for point in pop:
        original_obj = point.evaluate(algo.problem)
        mutant = algo.mutate(point, pop)
        if not algo.problem.check_constraints(mutant):
          continue
        mutated_obj = mutant.evaluate(algo.problem)
        if algo.dominates(mutated_obj, original_obj) and (not mutant in clones):
          clones.remove(point)
          clones.append(mutant)
      pop = clones
      gen += 1
    if RANK == 0:
      for i in range(1, SIZE):
        pop += COMM.recv(source=i, tag = id)
      return pop
    else:
      COMM.send(pop, dest=0, tag = id)