# %load q01_chocolates/build.py


input_list = []
def q01_chocolates(my_list=input_list):
    list1=[]
    z=0
    for i in my_list:
        if i%2==1:
            z+=i
        list1.append(z)
    return list1







