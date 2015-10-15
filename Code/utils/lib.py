"""
Standard library files and operators
"""
from __future__ import print_function, division
import random
import sys
import math

# Constants
EPS = 0.00001
PI = math.pi

class O():
  """
  Default class which everything extends.
  """
  def __init__(i,**d): i.has().update(**d)
  def has(i): return i.__dict__
  def update(i,**d) : i.has().update(d); return i
  def __repr__(i)   :
    show=[':%s %s' % (k,i.has()[k])
          for k in sorted(i.has().keys() )
          if k[0] is not "_"]
    txt = ' '.join(show)
    if len(txt) > 60:
      show=map(lambda x: '\t'+x+'\n',show)
    return '{'+' '.join(show)+'}'
  def __getitem__(i, item):
    return i.has().get(item)

def norm(x, low, high):
  """
  Normalize Value
  :param x: Value to be normalized
  :param low: Minimum value
  :param high: Maximum value
  :return: Normalized value
  """
  nor = (x - low)/(high - low + EPS)
  if nor > 1:
    return 1
  elif nor < 0:
    return 0
  return nor


def de_norm(x, low, high):
  """
  De-normalize value
  :param x: Value to be denormalized
  :param low: Minimum value
  :param high: Maximum value
  :return:
  """
  de_nor = x*(high-low) + low
  if de_nor > high:
    return high
  elif de_nor < low:
    return low
  return de_nor

def uniform(low, high):
  """
  Uniform value between low and high
  :param low: minimum of distribution
  :param high: maximum of distribution
  :return: Uniform value in the uniform distribution
  """
  return random.uniform(low, high)

def say(*lst):
  """
  Print value on the same line
  :param lst:
  :return:
  """
  print(*lst, end="")
  sys.stdout.flush()

def choice(lst):
  """
  Return random value from list
  :param lst: list to search in
  :return:
  """
  return random.choice(lst)

def more(x,y):
  """
  Check if x > y
  :param x: Left Comparative Value
  :param y: Right Comparative Value
  :return: Boolean
  """
  return x > y

def less(x,y):
  """
  Check if x < y
  :param x: Left Comparative Value
  :param y: Right Comparative Value
  :return: Boolean
  """
  return x < y

def avg(lst):
  """
  Average of list
  :param lst:
  :return:
  """
  return sum(lst)/float(len(lst))

def cos(val):
  """
  Return cosine of a value
  :param val: Value in radians
  :return:
  """
  return math.cos(val)

def sin(val):
  """
  Return sine of a value
  :param val: Value in radians
  :return:
  """
  return math.sin(val)

class Point(O):

  def __init__(self, decisions, problem=None):
    """
    Represents a point in the frontier for NSGA
    :param decisions: Set of decisions
    :param problem: Instance of the problem
    :param do_eval: Flag to check if evaluation has to be performed
    """
    O.__init__(self)
    self.decisions = decisions
    if problem:
      self.objectives = problem.evaluate(decisions)
    else:
      self.objectives = []

  def clone(self):
    """
    Method to clone a point
    :return:
    """
    new = Point(self.decisions)
    new.objectives = self.objectives
    return new

  def evaluate(self, problem):
    """
    Evaluate a point
    :param problem: Problem used to evaluate
    """
    if not self.objectives:
      self.objectives = problem.evaluate(self.decisions)

  def __eq__(self, other):
    return self.decisions == other.decisions

def report(lst, name):
  print("*** ", str.upper(name), " ***")
  s_lst = sorted(lst)
  low = s_lst[0]
  high = s_lst[-1]
  med = s_lst[len(lst)//2] if len(lst) % 2 else (s_lst[len(lst)//2] + s_lst[len(lst)//2 - 1])/2
  print("LOW  : ", low)
  print("HIGH : ", high)
  print("MED  : ", med)

