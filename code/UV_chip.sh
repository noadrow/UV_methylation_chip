#!/bin/bash

./blat -stepSize=5 -repMatch=2253 -minScore=20 -minIdentity=0 hg38.fa $1 output.psl
sed '1,5d' output.psl > newfile.txt
awk -F'\t' '{print $14 "\t" $9 "\t" $16 "\t" $17}' newfile.txt > arigent_sites.bed
python3 ./extened_bed.py arigent_sites.bed arigent_sites_extended.bed
bedtools getfasta -fi hg38.fa -bed arigent_sites_extended.bed > arigent_sites_extended.fa
python3 ./UV_chip.py arigent_sites_extended.fa arigent_1000_chip_test.txt
python3 ./plot_betas.py arigent_1000_chip_test.txt $2
