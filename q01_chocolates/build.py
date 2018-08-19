# %load q01_chocolates/build.py
input_list = [2, 5, 8, 11, 4]

# Write your solution here:

def q01_chocolates(my_list=input_list):
    result = []
    values = 0
    for data in my_list:
        if data % 2 != 0:
            values += data
            
        result.append(values)
    return result

print(q01_chocolates(input_list))


