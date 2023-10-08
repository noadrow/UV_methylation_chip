import pandas as pd
import sys


if(len(sys.argv) > 1):
    INPUT_control = str(sys.argv[1])
    OUTPUT_control = INPUT_control.replace('.bed','_extened.bed')
    length = int(sys.argv[2])
else:
    from tkinter import Tk
    from tkinter.filedialog import askopenfilename
    from tkinter.simpledialog import askstring, askinteger

    Tk().withdraw()
    INPUT_control = askopenfilename(title='Insert Bed file to extened')
    OUTPUT_control = INPUT_control.replace('.bed','_extened.bed')
    length = askinteger('Enter length to extened', 'Enter length to extened')

Control_list = []
Prog_list = []
Control_pos_list = ""
i = 0

for line_control in open(INPUT_control,"r"):
    Control_list.append(line_control.replace('\n',''))

for chunk in pd.read_csv(INPUT_control,sep='\t',header=0, on_bad_lines='skip').dropna().iterrows():
    chunk_chr = str(chunk[1][0]) + "\t"
    if(len(chunk[1])>3):
        if(chunk[1][1]=="+" or chunk[1][1]=="-"):
            chunk_starnd = str(chunk[1][1]) + "\t"
            chunk_start = str(int(chunk[1][2]) - length) + "\t"
            chunk_end = str(int(chunk[1][3]) + length) + "\t"
        else:
            chunk_starnd = ""
            chunk_start = str(int(chunk[1][1]) - length) + "\t"
            chunk_end = str(int(chunk[1][2]) + length) + "\t"

        if (len(chunk[1]) > 4):
            id = str(chunk[1][4]) + "\n"
        else:
            id = str(chunk[1][3]) + "\n"
    else:
        chunk_starnd = ""
        chunk_start = str(int(chunk[1][1]) - length) + "\t"
        chunk_end = str(int(chunk[1][2]) + length) + "\t"
        id = "\n"


    Control_pos_list += chunk_chr+chunk_starnd+chunk_start+chunk_end+id
    i = i + 1

    if (i > (len(Control_list) + len(Prog_list))):
        break

open(OUTPUT_control,"w").write(Control_pos_list)

