import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#import matplotlib; matplotlib.use('Qt5Agg')
from matplotlib import pyplot as plt
import pandas as pd
import os


def loading_file():
    import sys
    if(len(sys.argv) > 0):
        INPUT_control = str(sys.argv[1])
        return INPUT_control
    else:
        from tkinter import Tk
        from tkinter.filedialog import askopenfilename

        Tk().withdraw()
        INPUT_control = askopenfilename(title='Insert values list to plot')
        return INPUT_control

INPUT_control = loading_file()
OUTPUT_control = INPUT_control.replace('.csv','.png')

#INPUT_control = str(sys.argv[1])
#OUTPUT_control = str(sys.argv[2])
def plot_heatmap(df,even_matrix, save_path):

    #data = np.array(df)
    #plt.figure(figsize=(10, 8))  # You can adjust the width and height as needed

    sns.heatmap(df, annot=False, cmap="viridis", cbar=True, fmt='.1f',linewidth=.5)
    #sns.heatmap(df, annot=even_matrix, fmt="")

    if save_path:
        plt.title(os.path.basename(save_path))

    plt.savefig(save_path)
    #plt.show()

def list_to_even_matrix(input_list, fill_value=0):

    matrix_dim = int(len(input_list) ** 0.5)
    if matrix_dim * matrix_dim < len(input_list):
        matrix_dim += 1
    if(matrix_dim*matrix_dim > len(input_list)):
        to_add = matrix_dim*matrix_dim - len(input_list)
    else:
        to_add = 0

    input_list_2 = list(input_list)
    padded_list = input_list_2 + to_add*[fill_value]

    matrix = [padded_list[i:i+matrix_dim] for i in range(0, len(padded_list), matrix_dim)]

    return matrix


data = pd.read_csv(INPUT_control,header=0,delimiter=',',index_col=0)
data_int = data['sum'].values
id,sum,avg,min,max  = data.index.to_list(),data['sum'].values.tolist(),data['average'].values.tolist(),data['min'].values.tolist(),data['max'].values.tolist()
id_t = [i.split(":")[0] for i in id]
anno_list = [f"id:{id_t[i]} \n" +
             f" sum:{sum[i]} \n" +
             f"avg:{avg[i]} \n" +
             f"min:{min[i]} \n" +
             f"max:{max[i]}" for i in range(len(id))]

even_matrix = list_to_even_matrix(data_int)
df = pd.DataFrame(even_matrix)
even_matrix = list_to_even_matrix(anno_list)
# Plot the heatmap
plot_heatmap(df,even_matrix, save_path=OUTPUT_control)
