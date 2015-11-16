from __future__ import print_function, division
import sys
from problems.dtlz.dtlz2 import DTLZ2
from algorithms.serial.gale.gale import GALE as GALE_S
from algorithms.parallel.gale.gale import GALE as GALE_P
from algorithms.parallel.de.de import DE as DE_P
from mpi4py import MPI
from time import clock, sleep
from utils.lib import O, report
import utils.sk as sk


COMM = MPI.COMM_WORLD
RANK = COMM.rank
SIZE = COMM.size

settings = O(
  runs = 20
)

def _run_parallel():
  model = DTLZ2(3)
  opt = DE_P(model)
  times, convs, dives = [], [], []
  for i in range(settings.runs):
    print(i)
    start = clock()
    goods = DE_P.run(opt, id = i)
    if RANK == 0:
      times.append(clock() - start)
      convs.append(opt.convergence(goods))
      dives.append(opt.diversity(goods))
  if RANK == 0:
    print("Time", times)
    report(times, "Time Taken")
    print("Convergence", convs)
    report(convs, "Convergence")
    print("Diversity", dives)
    report(dives, "Diversity")



def _run_serial():
  times, convs, dives = [], [], []
  for i in range(settings.runs):
    model = DTLZ2(3)
    algo = GALE_S(model)
    start = clock()
    print(i)
    goods = algo.run()
    times.append(clock() - start)
    convs.append(algo.convergence(goods))
    dives.append(algo.diversity(goods))
    algo.solution_range(goods)
  print("Time", times)
  report(times, "Time Taken")
  print("Convergence", convs)
  report(convs, "Convergence")
  print("Diversity", dives)
  report(dives, "Diversity")

def _run_once(optimizer):
  model = DTLZ2(3)
  opt = optimizer(model)
  start = clock()
  goods = optimizer.run(opt)
  delta = clock() - start
  if RANK == 0:
    print("\nTime taken ", delta)
    print(opt.convergence(goods))
    print(opt.diversity(goods))
    opt.solution_range(goods)

DE_C_Serial = [2.5385316007181199e-05, 2.3418536994411972e-05, 2.3788062745336907e-05, 2.1613902083339628e-05, 2.3976668414068685e-05, 2.3596026056376446e-05, 2.0336834025242928e-05, 2.5909309176883238e-05, 2.0729672510416615e-05, 2.6585743373241287e-05, 2.1602981685093584e-05, 2.2346700949965269e-05, 2.2579422083628548e-05, 2.231760007548548e-05, 2.615552278660041e-05, 2.2513579763014682e-05, 2.2709449680334556e-05, 2.4915527333702019e-05, 2.4278665435833786e-05, 2.6885116330194885e-05]
DE_D_Serial = [0.465499451720295, 0.40800765137869721, 0.41641442775653548, 0.45459640279397984, 0.38857425158301789, 0.4046376492440143, 0.50246526623467103, 0.39077040010466046, 0.43069644523426481, 0.46197950806484039, 0.40565646468430328, 0.50496427308338288, 0.41009249104458678, 0.45683048772634699, 0.38733478737926141, 0.47260830992446817, 0.43135600173608601, 0.40976630540960923, 0.4022971036227318, 0.45361639362286515]

DE_C_Parallel = [2.2323387982126613e-05, 2.4333074285052263e-05, 2.2270526299816562e-05, 2.3205523162657712e-05, 2.1092276359523181e-05, 2.1407855944416968e-05, 2.2250669766713318e-05, 2.3678551985377964e-05, 2.1583718921410433e-05, 2.4863623824217972e-05, 2.5379584685899799e-05, 2.0447754571789871e-05, 2.1974415747496383e-05, 2.1509446263514352e-05, 2.624231879135836e-05, 2.3307973294286789e-05, 2.1527242139070658e-05, 2.4356868166740509e-05, 2.4135198439769288e-05, 2.3039512568492154e-05]
DE_D_Parallel = [0.36596662867535334, 0.39085625333137436, 0.3936334489416099, 0.409354079138461, 0.39286220542223804, 0.41727838941778106, 0.41326236850247028, 0.36838291446167198, 0.43363269728585985, 0.4447873881377204, 0.48831463037186568, 0.43315095399320308, 0.41757496045273962, 0.42088762553220677, 0.41099944934508381, 0.44280873094472162, 0.48157532327296509, 0.38815433861011767, 0.45849716800579426, 0.39495925576606855]

GALE_C_Serial = [0.00054903656622711254, 0.00054805945713180923, 0.00053022864630904664, 0.00055245599887427223, 0.00053916166432819361, 0.00056537970545386695, 0.00054323858105506532, 0.00055233217453614573, 0.00054624996601456007, 0.0005520676674477139, 0.00054883644295408425, 0.00055416323595685387, 0.0005576369915171347, 0.00054178547060682925, 0.00056097245871263328, 0.00054543518035334417, 0.00052320832020011387, 0.00055140278982456284, 0.00054678619596559494, 0.00055615838288943648]
GALE_D_Serial = [0.39767593653080563, 0.43134554250676654, 0.3724106193584652, 0.46492694431047593, 0.38114702887278101, 0.46412597957276913, 0.40136964424332505, 0.35958429832553424, 0.43754228630327224, 0.42960824185718016, 0.39595095997467389, 0.46074518209968807, 0.46397272534225492, 0.4313664485647285, 0.44472666191643639, 0.40330377421744662, 0.38374075237806826, 0.43714667994146489, 0.44456144648909562, 0.41217275174594703]

GALE_C_Parallel = [0.00055023804107289464, 0.00056840024193905369, 0.00054014713499315982, 0.00055388230660610781, 0.00055426400275676092, 0.00056243234904455105, 0.00056728935419035609, 0.00056880907130547561, 0.0005451698867692228, 0.00056076770918203633, 0.00055907200720460939, 0.00054222667029832816, 0.00056563411151671402, 0.00057999736847168964, 0.00054982625514456076, 0.00054568440322032416, 0.00053338609030626589, 0.00053350914975169178, 0.00053640243252309075, 0.00056947417926847879]
GALE_D_Parallel = [0.47756324201340233, 0.34338827152012313, 0.37702310652791976, 0.3812810382395399, 0.44246226377967579, 0.3918531310121483, 0.40870091345000326, 0.45126527598138111, 0.44627298181072489, 0.43102137690260817, 0.36304936983777769, 0.32840066997860679, 0.49015906974400514, 0.49534594905918372, 0.37685351425128155, 0.41589424177536238, 0.44379976457351544, 0.39392598613842977, 0.41257192127627285, 0.4664020477306397]


def _stat():
  sk.rdivDemo([
    ["DE_S"] + DE_D_Serial,
    ["DE_P"] + DE_D_Parallel,
    ["GALE_S"] + GALE_D_Serial,
    ["GALE_P"] + GALE_D_Parallel
  ])

if __name__ == "__main__":
  # args = sys.argv
  # if len(args) != 2:
  #   print("Optimizer not mentioned")
  #   exit()
  # if args[1] == "gale":
  #   _run_once(GALE_P)
  # elif args[1] == "de":
  #   _run_once(DE_P)
  _run_parallel()