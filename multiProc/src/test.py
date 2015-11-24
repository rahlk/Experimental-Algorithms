# from __future__ import print_function, division
import os
import sys
import subprocess
from multiprocessing import Pool, Process
from time import  sleep
# Get the git root directory
root_dir=repo_dir = subprocess.Popen(['git'
                                      ,'rev-parse'
                                      , '--show-toplevel']
                                     , stdout=subprocess.PIPE
                                     ).communicate()[0].rstrip()
sys.path.append(root_dir)


def func(arg):
  sleep(0.1)
  return arg**2

def info(title):
    print title
    print 'module name:', __name__
    if hasattr(os, 'getppid'):  # only available on Unix
        print 'parent process:', os.getppid()
    print 'process id:', os.getpid()

def f(name):
    info('function f')
    print 'hello', name

if __name__=="__main__":
  # info('main line')
  # p = Process(target=f, args=('bob',))
  # p.start()
  # p.join()

  p=Pool(processes=5)
  p.apply_async(func, range(100))
  ret = p.map(func, range(100), chunksize=10)
  print ret
