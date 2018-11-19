# %load q01_chocolates/build.py


input_list = []

# Write your solution here:


def q01_chocolates(my_list=input_list):
    output_list = []
    count = 0
    for i in my_list:
        if(i%2!=0):
            count+=i
        output_list.append(count)
    return output_list





