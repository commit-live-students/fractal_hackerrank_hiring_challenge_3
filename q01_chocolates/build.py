# %load q01_chocolates/build.py


input_list = []

def q01_chocolates(my_list):
    value = 0 
    new = []
    for i in my_list:
        if i % 2 != 0:
            value += i
            new.append(value)
        if i % 2 == 0:
            new.append(value)
    return new


    







