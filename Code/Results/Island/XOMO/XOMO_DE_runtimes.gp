# For PNG
set terminal png
set output "XOMO_DE_runtimes.png"

# For EPS
# set terminal eps
# set output "XOMO_DE_runtimes.eps"

set title "Runtimes"

set xlabel " Processors "

set ylabel " Runtime (sec) "

set xrange [0:17]

set datafile separator ","

plot for [col=3:3] "XOMO_GALEvsDE.csv" using 1:col with lines title columnheader