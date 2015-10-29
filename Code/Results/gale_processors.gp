set terminal png

set output "gale_processors.png"

set title "GALE"

set xlabel " Processors "

set ylabel " Runtime(seconds) "

set xrange [1:]

set datafile separator ","

plot "gale_processors.csv" using 1:2 title 'GALE'