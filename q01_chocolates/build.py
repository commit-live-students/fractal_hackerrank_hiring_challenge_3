# %load q01_chocolates/build.py


input_list = [3, 4, 5, 8, 9, 10]

# Write your solution here:


def q01_chocolates(my_list=input_list):
    result = []
    sum_of_chocolates = 0
    for data in my_list:
        if data % 2 != 0:
            sum_of_chocolates += data
            
        result.append(sum_of_chocolates)
    
    return result







