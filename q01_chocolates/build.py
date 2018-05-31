# %load q01_chocolates/build.py


input_list = []

# Write your solution here:


def q01_chocolates(my_list=input_list):
    output_list=list()
    choc=0
    for lst in my_list:
        if(lst%2!=0):
            choc+=lst
        output_list.append(choc)
    return output_list




