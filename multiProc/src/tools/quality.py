from __future__ import division, print_function
from scipy.spatial.distance import euclidean
from numpy import mean
from pdb import set_trace

class measure:
  def __init__(self,model):
    self.mdl = model

  def convergence(self, obtained):
    """
    Calculate the convergence metric with respect to ideal
    solutions
    """
    gammas=[]
    ideals = self.mdl.get_pareto()
    def nearest(a,lst):
      # dist = euclidean(a, sorted(lst, key=lambda x:euclidean(x,a))[0])
      # set_trace()
      return euclidean(a, sorted(lst, key=lambda x:euclidean(x,a))[0])
    gammas = [nearest(self.mdl.solve(member),ideals) for member in obtained]
    return mean(gammas)