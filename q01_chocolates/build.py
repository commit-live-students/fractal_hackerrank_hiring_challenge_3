# %load q01_chocolates/build.py


input_list = []

# Write your solution here:


def q01_chocolates(my_list):
    x=0
    result=[]
    for i in my_list:
        if i%2!=0:
            x=x+i
        else:
            x=x
        result.append(x)   
        #print (x)
        #print(list2)
    return result

print (q01_chocolates([1,2,5,8]))










