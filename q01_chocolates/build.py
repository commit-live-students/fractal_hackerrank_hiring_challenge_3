# %load q01_chocolates/build.py
input_list = []
# Write your solution here:
def q01_chocolates(days=input_list):
    sum = 0
    sum_of_chocolates = []
    
    for day in days:
        if day % 2 != 0:
            sum = sum + day
        sum_of_chocolates.append(sum)
        
    return sum_of_chocolates


