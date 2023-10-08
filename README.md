# UV_methylation_chip
![alt text]([http://url/to/img.png](https://github.com/noadrow/UV_methylation_chip/blob/9038c37f76b701f159557feca85f1c808a198c16/UV.png))

# UV_CHIP.pptx
Summary of the algorithm's simulation and results

# code folder
## average_meth.py
A Python script takes a methylation dataset and a chosen CpG list as input and outputs the mean, standard deviation, maximum, and minimum values.

## blat.sh
A bash script that converts CpG sites into FASTA format and also extends the range by 2 nucleotides to 1000 on each side (useful for simulation purposes - range for the target selection)

## extened_bed.py 
A Python script that adds a chosen number of nucleotides to each side.

## extened_bed.sh
A bash script that adds a chosen number of nucleotides to each side of the sequence (recommended for speed efficiency)

## get_probes_arigent.py
A Python script that specifically parses the Agilent probe sites to generate a fasta-formatted list of sites.

## label_seq.py
A Python script designed to label CpG sites within a string (unfinished).

## main.py 
a python script: UV chip simulation version_1
calculate expected flourence distribution in a fully un-methylated state.

## main_2.py
A Python script, UV chip simulation version 1, calculates the expected fluorescence distribution in a fully unmethylated state sites.

## mult_nums.sh
An executable bash script that processes a file containing simulation values and computed beta-values from an Illumina dataset, performing multiplication on these values.

## plot_betas.py
A Python script that takes the simulation results (or any list of numbers), shapes them into an M x M matrix, and colors the heatmap based on the values.

## UV_chip.py
The final official script that calculates the simulation values for the UV chip array.

## UV_chip.sh
A bash script representing the nearly complete pipeline, starting from the position of the CpG sites and ending with the generation of the simulation results plot.

## UV_chip_2.ipynb
A Jupyter notebook documenting the initial stages of the simulation script.

# DATA folder
All data used for the project:
## 60k_array_probe_analysis:
  Source of original Agilent probe sequences.
## arigent_sites:
  Agilent 60k array probe sequences in FASTA format (also indexed).
## hg38.fa: 
  The genome reference used for this experiment.
## horvrath_clock.bed: 
  BED format file containing the 334 CpG sites found in the Horvath clock.
## horvrath_clock.txt:
  The list of CpG sites in the Horvath clock."

* note: you'll might want to use unix2dos function before using the bash scripts on windows.
