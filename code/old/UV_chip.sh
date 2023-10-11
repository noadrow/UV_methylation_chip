#!/bin/bash

## extract genome position from sequences
./blat -stepSize=5 -repMatch=2253 -minScore=20 -minIdentity=0 ../data/hg38.fa $1 output.psl
sed '1,5d' output.psl > newfile.txt
## parse to BED format
awk -F'\t' '{print $14 "\t" $9 "\t" $16 "\t" $17}' newfile.txt > arigent_sites.bed 
# extened BED format for simulation 
# 1000bp for each side
python3 ./extened_bed.py arigent_sites.bed 1000 ../data/hg38.fa
bedtools getfasta -fi ../data/hg38.fa -bed arigent_sites_extended.bed > arigent_sites_extended.fa
python3 ./UV_chip.py arigent_sites_extended.fa 1000
python3 ./plot_betas.py arigent_sites_extended.csv




