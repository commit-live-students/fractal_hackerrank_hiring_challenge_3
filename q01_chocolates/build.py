# %load q01_chocolates/build.py


input_list_1 = [3, 4, 5, 8, 9, 10]
input_list_2 = [2, 5, 8, 11, 4]

# Write your solution here:


def q01_chocolates(my_list):
    a=my_list
    res=[]
    count1=0
    for i in range(len(a)):
        if a[i]%2 !=0:
            b=a[i]
            count1+=b
            res.append(count1)
        else: #a[i]%2==0:
            b=0
            count1=count1+b
            res.append(count1)
    return res
            
            
            





my_list= [3, 4, 5, 8, 9, 10]
c=q01_chocolates(my_list)
c
my_list = [2, 5, 8, 11, 4]
c=q01_chocolates(my_list)
c


