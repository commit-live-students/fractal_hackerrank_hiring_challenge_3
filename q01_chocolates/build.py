# %load q01_chocolates/build.py

import numpy as np

# Write your solution here:

def q01_chocolates(my_list):
    input_list = [0]
    for num in my_list:
        if num % 2 == 0 :
            input_list.append(input_list[-1])
        else:
            input_list.append(input_list[-1] + num)
    input_list.pop(0)
    return input_list






