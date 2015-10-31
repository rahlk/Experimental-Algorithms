# For PNG
# set terminal png
# set output "gale_processors.png"

# For EPS
set terminal eps
set output "gale_processors.eps"

set title "GALE"

set xlabel " Processors "

set ylabel " Runtime (seconds) "

set xrange [1:]

set datafile separator ","

plot "gale_processors.csv" using 1:2 lt 1 lw 2 smooth bezier title 'GALE'