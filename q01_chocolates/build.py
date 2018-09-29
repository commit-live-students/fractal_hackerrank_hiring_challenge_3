# %load q01_chocolates/build.py


input_list = []


# Write your solution here:


def q01_chocolates(my_list=input_list):

    b=[x if x%2==1 else 0 for x in my_list]
    
    new_l=[]
    cumsum=0
    for i in b:
        cumsum += i
        new_l.append(cumsum)
        
    return new_l





