# %load q01_chocolates/build.py


input_list = []

# Write your solution here:


def q01_chocolates(my_list=input_list):
    output_list =[]
    su = 0
    for i in my_list:
        if i%2 !=0:
            output_list.append(su + i)
            su = su + i
        else:
            output_list.append(su)
    return output_list
            
            





input_list_2 = [2, 5, 8, 11, 4]
q01_chocolates(input_list_2)
output_list =[]
su = 0
for i in input_list_2:
    if i%2 !=0:
        output_list.append(su + i)
        su = su + i
    else:
        output_list.append(su)
   
output_list


