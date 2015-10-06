from __future__ import print_function, division
import sys
sys.path.append('..')
from sklearn import svm
from pdb import set_trace
from collections import Counter
import random
from numpy import array, sum
from random import choice as any
from ABCD import ABCD

__author__ = 'rkrsn'
class o:
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

def say(l):
  sys.stdout.write(str(l))

def params(**d):
  """
  RTFM please - http://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC
  """
  return o(
    C = (1e-2,1, float), # Penalty parameter C of the error term.
    tol = (1e-2,1, float), # Tolerance for stopping criteria.
    fit_intercept=(True, False, bool), # Whether to calculate the intercept for this model.
    # If set to false, no intercept will be used in calculations (e.g. data is expected to be already centered).
    scaling = (1e-2,1, float),
    max_iter = (1, 1e4, int),
    shrinking = (True, False, bool)).update(**d)
    # degree = (2,10,int),
    # gamma = (0,1,float),
    # kernel = ('linear', 'rbf', 'poly', 'sigmoid', str),

def settings(**d):
  return o(
      name="Differention Evolution",
      what="DE tuner. Tune the planner parameters.",
      author="Rahul Krishna",
      copyleft="(c) 2014, MIT license, http://goo.gl/3UYBp",
      seed=1,
      np=10,
      k=100,
      tiny=0.01,
      de=o(
          iter=50,
          N=100,
          f=0.75,
          cf=0.5,
          maxIter=100,
          lives=10)).update(
      **d)

def SVM(train, test, tunings=None):
  if not tunings:
    clf = svm.LinearSVC()
      # kernel='linear')
  else:
    clf = svm.LinearSVC(
      # kernel='linear',
      # kernel=tunings[5],
      # degree=tunings[6],
      # gamma=tunings[7],
      # shrinking=tunings[8],
      C=tunings[0],
      tol=tunings[1],
      fit_intercept =tunings[2],
      intercept_scaling = tunings[3],
      # gamma = tunings[3],
      max_iter = tunings[4])
  features = [f for f in train.columns if not f == '$CLASS']
  klass = train['$CLASS']
  clf.fit(train[features], klass)
  return clf.predict(test[features])


class diffEvol(object):

  """
  Differential Evolution
  """

  def __init__(i, model):
    i.frontier = []
    i.model = model
    i.xbest = []
    i.settings = settings().de

  def new(i):
    # Creates a new random instance
    rand = lambda d: random.choice([True, False]) if d[2]==bool else d[2](random.uniform(d[0], d[1]))
    return [rand(d) for d in i.model.indep()]

  def initFront(i, N):
    # Initialize frontier
    for _ in xrange(N):
      i.frontier.append(i.new())

  def extrapolate(i, xbest, l1, l2):
    def extrap(y,z,a,d):
      if d[2]==bool:
        return z==a if random.random()>i.settings.cf else a
      else:
        return  d[2](max(d[0], min(d[1], y + i.settings.f * (z - a)))) if random.random()>i.settings.cf else d[2](a)
    return [extrap(y,z,a,d) for y, z, a,
            d in zip(xbest, l1, l2, i.model.indep())]

  def one234(i, one, pop, f=lambda x: id(x)):
    def oneOther():
      try: x = any(pop)
      except: set_trace()
      while f(x) in seen:
        x = any(pop)
      seen.append(f(x))
      return x
    seen = [f(one)]

    return oneOther(), oneOther()

 # def top234(i, one, pop):

  def dominates(i, one, two):
    #     set_trace()
    return i.model.depen(one) > i.model.depen(two)

  def dominates2(i, one, two):
    "Binary Domination"
    #     set_trace()
    return i.model.depen(
        one)[0] > i.model.depen(
        two)[0] and i.model.depen(
        one)[1] > i.model.depen(
        two)[1]

  def sortbyscore(i):
    return sorted(
        i.frontier, key=lambda F: i.model.depen(F), reverse=True)

  def DE(i):
    i.initFront(i.settings.N)
    lives = i.settings.lives
    iter = 0
    while lives > 0 and iter < 30:
      better = False
      i.xbest = i.sortbyscore()[0]
      for pos in xrange(len(i.frontier)):
        iter += 1
        lives -= 1
        l1, l2 = i.one234(i.frontier[pos], i.frontier)
        new = i.extrapolate(i.xbest, l1, l2)
        if i.dominates(new, i.frontier[pos]):
          i.frontier.pop(pos)
          i.frontier.insert(pos, new)
          better = True
          lives += 1
          if i.model.depen(new) > i.model.depen(i.xbest):
            i.xbest = new
        elif i.dominates(i.frontier[pos], new):
          better = False
          if i.model.depen(
                  i.frontier[pos]) > i.model.depen(
                  i.xbest):
            i.xbest = i.frontier[pos]
        else:
          i.frontier.append(new)
          if i.model.depen(new) > i.model.depen(i.xbest):
            i.xbest = new
          better = True
          lives += 1
    return i.xbest


class tuneSVM(object):
  """
  Tunes a Linear SVM
  """

  def __init__(i, train, test):
    i.train = train # !! Change this !!
    i.test = test # !! Change this !!

  def any(i):
    rand = lambda d: random.choice([True, False]) if d[2]==bool else d[2](random.uniform(d[0], d[1]))
    return [rand(d) for d in i.indep()]
  def depen(i, rows):
    mod = SVM(i.train, i.test, tunings=rows)
    actual = i.test['$CLASS']
    abcd = ABCD(before=actual, after=mod)
    F = array([k.stats()[1:-3] for k in abcd()])
    tC = Counter(actual)
    FreqClass=[tC[kk]/len(actual) for kk in list(set(actual))]
    # set_trace()
    ExptF = sum(F*FreqClass, axis=0)
    return ExptF

  def indep(i):
    P = params()
    return [
        P.C, # Penalty parameter C of the error term.
        P.tol, # Tolerance for stopping criteria.
        P.fit_intercept, # Whether to calculate the intercept for this model.
        # If set to false, no intercept will be used in calculations (e.g. data is expected to be already centered).
        P.scaling,
        P.max_iter]

def _test(train, test):
  m = tuneSVM(train, test)
  vals = [(m.any()) for _ in range(10)]
  vals1 = [m.depen(v) for v in vals]
  print(vals, vals1)
