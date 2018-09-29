# %load q01_chocolates/build.py


input_list = []

# Write your solution here:


def q01_chocolates(my_list=input_list):
    y=[]
    z=0
    for i in my_list:
        if i%2==1:
            z+=i  
        y.append(z)
    return y
    

q01_chocolates([3,4,5,8,9,10])


