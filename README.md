# UV_methylation_chip

# code folder
## average_meth.py
a python script takes a methylation dataset and a chosen CpG list and outputs mean\std\max\min

## blat.sh
a bash script that convert CpG sites into fasta and also extending the range from 2 nuclotised to 1000 from each side (usful for the simulation).

## extened_bed.py 
a python script that add a choosen number of nucleotides from each sides

## extened_bed.sh
a bash script that add a choosen number of nucleotides from each sides
(recommened, speed wise).

## get_probes_arigent.py
a python script that specificly parse the agilent probe sites to get a fasta formeted list.

## label_seq.py (not finished)
a python script made to label CpG sites in a string (not finished).

## main.py 
a python script: UV chip simulation version_1
calculate expected flourence distribution in a fully un-methylated state.

## main_2.py
a python script: UV chip simulation version_2
calculate expected flourence distribution in a fully un-methylated state.

## mult_nums.sh
a bash script that takes a file of simulation value and calculated beta-values from a illumina dataset and multiplied them.

## plot_betas.py
a python script that takes the simulation results (or any list of numbers) shape it to a M x M matrix and heatmap color by the value.

## UV_chip.py
The final offical script that calculate the simulation values of the UV chip array. 

## UV_chip.sh
A bash script of the almost full pipeline from the position of the CpG sites to the plotting of the simulation results. 

## UV_chip_2.ipynb
A jupyter notebook of the early stages of the simulation script.

# DATA folder
all data used for the project:
## 60k_array_probe_analysis:
  original agilent probe sequences source
## arigent_sites:
  60k_array_probe of agilent as a fasta format (also indexed)
## hg38.fa: 
  the genome reference used for this experiment.
## horvrath_clock.bed: 
  Bed format of the 334 CpG sites that found in the horvrath clock 

## horvrath_clock.txt:
  Just the CpG list itself of the horvarth clock

# results_1 folder



* note: you'll might want to use unix2dos function before using the bash scripts on windows.
