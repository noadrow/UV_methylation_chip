#intersections
#bedtools intersect -a $1 -b $2 > out1.bed
#bedtools intersect -a $1 -b $2 > out2.bed
new_name=${$1%.*}_extended.bed

python3 ../code/extened_bed.py $1 $new_name 1000

