# For PNG
set terminal png
set output "ERS_speedups.png"

# For EPS
# set terminal eps
# set output "ERS_speedups.eps"

set title "Speedups"

set xlabel " Processors "

set ylabel " Speedup "

set xrange [0:17]

set datafile separator ","

set key left top

plot for [col=4:5] "ERS_GALEvsDE.csv" using 1:col with lines title columnheader