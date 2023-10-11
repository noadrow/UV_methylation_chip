import pandas as pd
import sys
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
import os

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing

#INPUT_control = str(sys.argv[1])
#OUTPUT_control = str(sys.argv[2])

cg_path = askopenfilename(title="cg list")
meth_path = askopenfilename(title="methylation table")

df = pd.read_csv(cg_path,sep="\t")

cgs  = df.iloc[:,0].values
meth_df = pd.read_csv(meth_path, index_col=0)
filt_cgs = meth_df.index.intersection(cgs)

sums = meth_df[meth_df.index.isin(filt_cgs)].T.sum().values
means = meth_df[meth_df.index.isin(filt_cgs)].T.mean().values
mins = meth_df[meth_df.index.isin(filt_cgs)].T.min().values
maxes = meth_df[meth_df.index.isin(filt_cgs)].T.max().values

new_df = pd.DataFrame({"id":filt_cgs,
                       "sum":sums,
                       "average":means,
                       "min":mins,
                       "max":maxes})
new_df.index = new_df['id']

new_df.to_csv(f"{os.path.dirname(meth_path)}/test1_cgs.csv")
