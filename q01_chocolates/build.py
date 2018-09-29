# %load q01_chocolates/build.py


input_list = [3,4,5,8,9,10,11]

# Write your solution here:


def q01_chocolates(my_list=input_list):
    l=0
    p=[]
    for x in my_list:
        if x%2==1:
            l=l+x
        p.append(l)
    return p


q01_chocolates(input_list)
    




