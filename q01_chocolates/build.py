# %load q01_chocolates/build.py


input_list = []

# Write your solution here:


def q01_chocolates(my_list=input_list):

    List = []
    total = 0
    previous = 0
    for num in my_list:
        if(num % 2 != 0):
            total = total + num
            previous = total
            List.append(total)
        else:
            List.append(previous)
    
    return List


