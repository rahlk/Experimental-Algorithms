set terminal png

set output "de_processors.png"

set title "Differential Evolution"

set xlabel " Processors "

set ylabel " Runtime(seconds) "

set xrange [1:]

set datafile separator ","

plot "de_processors.csv" using 1:2 title 'DE'