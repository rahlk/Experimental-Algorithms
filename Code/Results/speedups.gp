# For PNG
set terminal png
set output "speedups.png"

# For EPS
# set terminal eps
# set output "de_processors.eps"

set title "Speed Up"

set xlabel " Processors "

set ylabel " Speedup "

set xrange [0:17]

set datafile separator ","

plot for [col=2:3] "speedups.csv" using 1:col with lines title columnheader