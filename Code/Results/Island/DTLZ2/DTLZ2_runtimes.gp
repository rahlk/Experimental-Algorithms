# For PNG
set terminal png
set output "DTLZ2_runtimes.png"

# For EPS
# set terminal eps
# set output "DTLZ2_runtimes.eps"

set title "Runtimes"

set xlabel " Processors "

set ylabel " Runtime (sec) "

set xrange [0:17]

set datafile separator ","

plot for [col=2:3] "DTLZ2_GALEvsDE.csv" using 1:col with lines title columnheader