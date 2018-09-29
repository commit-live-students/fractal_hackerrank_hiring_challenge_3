# %load q01_chocolates/build.py


input_list = [3,4,5,8,9,10]

# Write your solution here:

#Actual question is to 

def q01_chocolates(my_list=input_list):
    y = []
    z=0
    for v in my_list:
        if v%2==1:
            z+=v
        y.append(z)  
    return y
    
q01_chocolates(input_list)


