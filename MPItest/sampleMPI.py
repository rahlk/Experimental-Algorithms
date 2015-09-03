from mpi4py import MPI

comm=MPI.COMM_WORLD

rank=comm.rank
size=comm.size

for h in xrange(400):
  data = j**2
  comm.send(data, dest=(rank+1)%size)
  data1=comm.recv(source=(rank-1)%size)
  print data
  print
