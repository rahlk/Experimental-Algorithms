# For PNG
set terminal png
set output "de_processors.png"

# For EPS
# set terminal eps
# set output "de_processors.eps"

set title "Differential Evolution"

set xlabel " Processors "

set ylabel " Runtime (seconds) "

set xrange [1:]

set datafile separator ","

plot "de_processors.csv" using 1:2 lt 1 lw 2 smooth bezier title 'DE'