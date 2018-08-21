# %load q01_chocolates/build.py


input_list = [1,2,5,8]

# Write your solution here:

def q01_chocolates(my_list=input_list):
    lists=[]
    values=0
    for data in my_list:
        if data %2!=0:
            values+=data
            
        lists.append(values)
        
    return (lists)





print(q01_chocolates(input_list))


