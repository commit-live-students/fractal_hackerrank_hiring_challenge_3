# %load q01_chocolates/build.py
import pandas as pd
import numpy as np

input_list = [3, 4, 5, 8, 9, 10]
#input_list = [2, 5, 8, 11, 4]
# Write your solution here:


def q01_chocolates(my_list):

    val = 0
    final_list = []

    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            final_list.append(val)
        else:
            my_list[i] % 2 != 0
            val += my_list[i]
            final_list.append(val)
    return final_list
q01_chocolates(input_list)
#np.cumsum(input_list)


