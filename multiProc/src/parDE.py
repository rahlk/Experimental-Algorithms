from __future__ import print_function, division

import os
from demo import *
import subprocess
import sys
sys.path.append(os.path.abspath('../problems/'))
# Get the git root directory
root=repo_dir = subprocess.Popen(['git'
                                      ,'rev-parse'
                                      , '--show-toplevel']
                                      , stdout=subprocess.PIPE
                                    ).communicate()[0].rstrip()

sys.path.append(root)
from pdb import set_trace
from dtlz2 import DTLZ2
from multiprocessing import Pool
import random
from random import seed as rseed, randint as randi
import numpy as np
from time import time
from tools.quality import measure

class settings:
  iter=50,
  N=100,
  f=0.5,
  cf=0,
  maxIter=100,
  lives=10

def flatten(x):
  """
  Takes an N times nested list of list like [[a,b],[c, [d, e]],[f]]
  and returns a single list [a,b,c,d,e,f]
  """
  result = []
  for el in x:
    if hasattr(el, "__iter__") and not isinstance(el, basestring):
      result.extend(flatten(el))
    else:
      result.append(el)
  return result

def de0(model=DTLZ2(n_dec=30,n_obj=3), new=[], pop=int(1e4), iter=1000, lives=5, settings=settings):
  """
  Recursive FASTMAP clustering.
  """
  frontier = model.generate(pop)
  N = np.shape(frontier)[0]
  leaf = []
  norm = np.max(frontier, axis=0) - np.min(frontier, axis=0)

  def cdom(x, y, better=['less','less','less']):

    def loss1(i,x,y):
      return (x - y) if better[i] == 'less' else (y - x)

    def expLoss(i,x,y,n):
      return np.exp(loss1(i,x,y) / n)

    def loss(x, y):
      n      = min(len(x), len(y)) #lengths should be equal
      losses = [expLoss(i,xi,yi,n) for i, (xi, yi) in enumerate(zip(x,y))]
      return sum(losses)/n

    "x dominates y if it losses least"
    return loss(x,y) < loss(y,x)


  def extrapolate(current, l1, l2, l3):
    def extrap(a,x,y,z):
      return (max(0, min(1, x + settings.f * (z - y)))) if random.random()>settings.cf else a
    return [extrap(a,x,y,z) for a, x, y, z in zip(current, l3, l1, l2)]

  def one234(one, pop):
    ids = [i for i,p in enumerate(pop) if not p==one]
    a = np.random.choice(ids, size=3, replace=False)
    return one, pop[a[0]], pop[a[1]], pop[a[2]]

  while lives > 0 and iter>0:
    better = False
    xbest = random.choice(frontier)
    xbestVal = model.solve(xbest)
    for pos in xrange(len(frontier)):
      # print("Iterations:",iter)
      iter -= 1
      lives -= 1
      # t=time()
      now, l1, l2, l3 = one234(frontier[pos], frontier)
      # print("Time", time()-t)
      # set_trace()
      new = extrapolate(now, l1, l2, l3)
      newVal=model.solve(new)
      oldVal=model.solve(now)
      if cdom(newVal, oldVal):
        frontier.pop(pos)
        frontier.insert(pos, new)
        lives += 1
        # if newVal > xbestVal:
        #   xbest = new
        #   xbestVal = model.solve(xbest)
      elif cdom(model.solve(frontier[pos]), model.solve(new)):
        better = False
        # if oldVal > xbestVal:
        #   xbest = frontier[pos]
        #   xbestVal = model.solve(xbest)
      else:
        frontier.append(new)
        lives += 1
        # if newVal > xbestVal:
        #   xbest = new
        #   xbestVal = model.solve(xbest)
  return frontier
 
def de1(iter=1000,pop=100,model=DTLZ2(n_dec=30, n_obj=3)):
  n_proc = int(1000/iter)
  return de0(model,new=[],pop=int(pop/n_proc),iter=iter/n_proc)

def dEvol(n_proc=10,frontSize=1000,iters=1000):
  t = time()
  collect=[]
  final = []
  per = [iters/n_proc]*n_proc
  popSize = [frontSize/n_proc]*n_proc
  p=Pool(processes=n_proc)
  collect.extend(p.map(de1, per))
  for cc in collect: final.extend(cc)
  print("Time taken: ",time()-t)
  # true = DTLZ2(n_dec=30, n_obj=3).get_pareto()
  m = measure(model=DTLZ2(n_dec=30, n_obj=3))
  conv = m.convergence(final)
  print("Convergence:",conv)
  # set_trace()
  return

if __name__=="__main__":
  # de1()
  eval(cmd())