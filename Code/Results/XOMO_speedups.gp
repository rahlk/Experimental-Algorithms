# For PNG
set terminal png
set output "XOMO_speedups.png"

# For EPS
# set terminal eps
# set output "XOMO_speedups.eps"

set title "Runtimes"

set xlabel " Processors "

set ylabel " Runtime (sec) "

set xrange [0:17]

set datafile separator ","

set key left top

plot for [col=4:5] "XOMO_GALEvsDE.csv" using 1:col with lines title columnheader