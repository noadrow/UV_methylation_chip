#!/bin/bash

# fasta to bed
## get position from seq

SECONDS=0
echo "initiating blat"
 ./code/blat -stepSize=5 -repMatch=2253 -minScore=20 -minIdentity=100 $1 $2 ./results/output.psl
echo "blat finished"
echo "run time: " $SECONDS "sec"

## clean results to bed format

SECONDS=0
echo "initating bed re-formatting"
sed '1,5d' ./reuslts/output.psl | awk -F'\t' '{print $14 "\t" $9 "\t" $16 "\t" $17 "\t" $10}' > ./results/agilent_sites.bed
echo "finished bed re-formatting"
echo "run time: " $SECONDS "sec"

# extened records for simulation
## extened record position as bed

SECONDS=0
echo "extending bed"
python3 ./code/extened_bed.py /results/agilent_sites.bed /results/agilent_sites_extended.bed 1000
echo "finished extending bed"
echo "run time: " $SECONDS "sec"

## get as extened fasta

SECONDS=0
echo "making extened fasta"
bedtools getfasta -fi $1 -bed /results/agilent_sites_extended.bed > /results/agilent_sites_extended.fa
echo "finished making extened fasta"
echo "run time: " $SECONDS "sec"

# run simulation

SECONDS=0
echo "starting simulation"
python3 ./code/UV_chip.py /results/agilent_sites_extended.fa 1000
echo "finished simulation"
echo "run time: " $SECONDS "sec"

# plot simulation results

SECONDS=0
echo "plotting results"
python3 ./code/plot_betas.py ./results/agilent_sites_extended.csv
echo "finished to plotting results"
echo "run time: " $SECONDS "sec"