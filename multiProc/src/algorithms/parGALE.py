"""
"""
from __future__ import print_function, division
import pandas as pd
from random import seed as rseed, randint as randi
import numpy as np

def where(data):
  """
  Recursive FASTMAP clustering.
  """
  rseed(0)
  if isinstance(data, pd.core.frame.DataFrame):
    data = data.as_matrix()
  if not isinstance(data, np.ndarray):
    raise TypeError('Incorrect data format. Must be a pandas Data Frame, or a numpy nd-array.')

  N = np.shape(data)[0]
  clusters = []
  norm = np.max(data, axis=0)[:-1] -np.min(data, axis=0)[:-1]

  def aDist(one, two):
    return np.sqrt(np.sum((np.array(one[:-1])/norm-np.array(two[:-1])/norm)**2))

  def farthest(one,rest):
    return sorted(rest, key=lambda F: aDist(F,one))[-1]

  def recurse(dataset):
    R, C = np.shape(dataset) # No. of Rows and Col
    # Find the two most distance points.
    one=dataset[randi(0,R-1)]
    mid=farthest(one, dataset)
    two=farthest(mid, dataset)

    # Project each case on
    def proj(test):
      a = aDist(one, test)
      b = aDist(two, test)
      c = aDist(one, two)
      return (a**2-b**2+c**2)/(2*c)

    if R<np.sqrt(N):
      clusters.append(dataset)
    else:
      _ = recurse(sorted(dataset,key=lambda F:proj(F))[:int(R/2)])
      _ = recurse(sorted(dataset,key=lambda F:proj(F))[int(R/2):])

  recurse(data)
  return clusters
