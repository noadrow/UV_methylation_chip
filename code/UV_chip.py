import numpy as np
import re
import sys
from datetime import datetime
import os

if(len(sys.argv) > 1):
    INPUT_control = str(sys.argv[1])
    OUTPUT_control = INPUT_control.replace('.fa','.csv')
    #rep = 1000
    rep = int(sys.argv[2])
else:
    from tkinter import Tk
    from tkinter.filedialog import askopenfilename
    from tkinter.simpledialog import askinteger

    Tk().withdraw()
    INPUT_control = askopenfilename(title='insert fasta input file')
    OUTPUT_control = INPUT_control.replace('.fa', '.csv')
    # rep = 1000
    rep = askinteger(title="number of simulation iterations", prompt="number of simulation iterations")

mean = 190
# var from the right
# 617(~mean+3std) - 190(mean) = 427/3
# std = 142.33
std_right = 142
min_len = 44
max_len = 617
beta_expected = 0.8
probe_size = 45
# beta_expected = 1
min_hib = 6
min_prob_loc, max_probe_loc = 0, 0

#INPUT_control = str(sys.argv[1])
#OUTPUT_control = str(sys.argv[2])
def probe_init(seq):
    global min_prob_loc, max_probe_loc
    seq_temp = re.sub('[^A-Za-z0-9]+', '', seq)
    seq_temp = seq_temp[1:-1]

    min_prob_loc = round((len(seq_temp) - 1) / 2 - probe_size / 2)
    max_probe_loc = round((len(seq_temp) - 1) / 2 + probe_size / 2)

    probe = seq_temp[min_prob_loc:max_probe_loc]

    return [seq_temp, probe]
def get_from_norm_len():
    y_values = np.random.normal(mean, std_right, 1)
    y_values = int(y_values[0])
    while(y_values<probe_size):
        y_values = np.random.normal(mean, std_right, 1)
        y_values = int(y_values[0])
    else:
        return y_values

# then we randomly select a subset which will be our specific "measured" event:
# DNA with a random length was connected to the probe on a random location
def get_random_substring(main_str):
    # for now it's a uniform distribution, but it can be replaced
    # substr_len = random.randint(min, max)

    substr_len = get_from_norm_len()
    idx_max = min_prob_loc
    idx_min = min_prob_loc - substr_len + probe_size
    if idx_min < min_prob_loc:
        idx = np.random.randint(idx_min, high=idx_max, size=1, dtype=int)[0]
    else:
        idx = min_prob_loc

    return [idx, main_str[idx: (idx + substr_len)]]
def calc_intensity(str, meth):
    if meth:
        return 0
    else:
        return str.count('CG') + str.count('cg')

def calc_vec(probe, meth):
    if meth:
        probe = probe.replace('CG', '00')
        probe = probe.replace('GC', '00')
        probe = re.sub('\D', '0', probe)
    else:
        probe = probe.replace('CG', '10')
        probe = probe.replace('GC', '01')
        probe = re.sub('\D', '0', probe)

    return [int(x) for x in probe]

def probe_expected_range(probe):
    probe_vec_meth = calc_intensity(probe, True)
    probe_vec_unmeth = calc_intensity(probe, False)

    meth_expected_val = probe_vec_meth * beta_expected
    unmeth_expected_val = probe_vec_unmeth * beta_expected

    return [meth_expected_val, unmeth_expected_val]
def run_that_ship_1(probe):
    idx, sample_probe = get_random_substring(probe)
    sim_unmeth = calc_intensity(sample_probe, False)
    return sim_unmeth, idx, len(sample_probe), sample_probe

def iter_sim(probe,rep):
    CGS = []
    for i in range(0, rep, 1):
        res = run_that_ship_1(probe)
        CGS.append(res[0])

    return [np.sum(CGS),np.average(CGS),np.min(CGS),np.max(CGS)]
def reverse_strand(probe):
    probe = probe.replace('C','1')
    probe = probe.replace('G', 'C')
    probe = probe.replace('T', '2')
    probe = probe.replace('A', 'T')
    probe = probe.replace('1', 'G')
    probe = probe.replace('2', 'A')
    return probe[::-1]

content = "id,sum,average,min,max\n"

for line in open(INPUT_control,"r"):
    if (">" in line):
        content = content + str(line.replace(">", "").replace("\n","")) + ","
    elif(">" not in line):
        seq_temp, probe = probe_init(line)
        seq_temp_rev = reverse_strand(seq_temp)
        res = iter_sim(seq_temp_rev, rep)
        content = content + str(res[0]) + "," + str(res[1]) + "," + str(res[2]) + "," + str(res[3]) + "\n"


open(OUTPUT_control,"w").write(content)
now = str(datetime.now()).replace(" ","_").replace(":","-")
folder_pos = os. path. dirname(OUTPUT_control)
open(f"{folder_pos}/log_{now}.txt","x").write(f"simulation number iteration: {rep}\n " +
                                 f"input file: {OUTPUT_control}\n " +
                                 f"output file: {INPUT_control}\n " )
