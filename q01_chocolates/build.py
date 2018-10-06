# %load q01_chocolates/build.py


input_list = []

# Write your solution here:

def q01_chocolates(my_list=input_list):
    new1 = []
    iprev = 0
    for i in my_list :
        if i % 2 == 1 :
            new1.append(i+iprev)
            iprev = i + iprev
        else:
            new1.append(iprev)
    return new1
   
    


