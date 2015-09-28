from __future__ import print_function, division
from problems.dtlz2 import DTLZ2

if __name__ == "__main__":
  model = DTLZ2()
  population = model.populate(20)
  for one in population:
    print("")
    print("Dec : ", one)
    print("Obj : ", model.evaluate(one))
