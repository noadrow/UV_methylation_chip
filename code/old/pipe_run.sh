#!/bin/bash

# fasta to bed
## get position from seq


#../code/blat -stepSize=5 -repMatch=2253 -minScore=20 -#minIdentity=0 ../data/hg38.fa $1 output.psl


SECONDS=0
echo "initiating blat"
../code/blat  -repMatch=1 -minScore=20 -minIdentity=100 ../data/hg38.fa $1 output.psl
echo "blat finished"
echo "run time: " $SECONDS "sec"

## clean results to bed format

SECONDS=0
echo "initating bed re-formatting"
sed '1,5d' output.psl | awk -F'\t' '{print $14 "\t" $9 "\t" $16 "\t" $17 "\t" $10}' > agilent_sites.bed
echo "finished bed re-formatting"
echo "run time: " $SECONDS "sec"

# extened BED format for simulation 
# 1000bp for each side

SECONDS=0
echo "extending bed"
python3 ./extened_bed.py arigent_sites.bed 1000 ../data/hg38.fa
echo "finished extending bed"
echo "run time: " $SECONDS "sec"

## get as extened fasta

SECONDS=0
echo "making extened fasta"
bedtools getfasta -fi ../data/hg38.fa -bed agilent_sites_extended.bed > agilent_sites_extended.fa
echo "finished making extened fasta"
echo "run time: " $SECONDS "sec"

# run simulation

SECONDS=0
echo "starting simulation"
python3 ./UV_chip.py arigent_sites_extended.fa 1000
echo "finished simulation"
echo "run time: " $SECONDS "sec"

# plot simulation results

SECONDS=0
echo "plotting results"
python3 ./plot_betas.py arigent_sites_extended.csv
echo "finished to plotting results"
echo "run time: " $SECONDS "sec"







