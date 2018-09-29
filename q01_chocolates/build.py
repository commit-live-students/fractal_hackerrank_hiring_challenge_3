# %load q01_chocolates/build.py


input_list = []

# Write your solution here:


def q01_chocolates(my_list = input_list):
    sum=0
    s=[]
    for x in my_list:
        if x%2 == 1:
            sum+=x
        s.append(sum)
    return s



