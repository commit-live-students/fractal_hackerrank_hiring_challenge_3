# %load q01_chocolates/build.py

input_list = [2, 5, 8, 11, 4]

# Write your solution here:
def q01_chocolates(my_list=input_list):
    '''Funtion to find the number of choclates'''
    
    output = []   #empty list

    #For loop
    for i,v in enumerate(my_list): 
        if v%2 != 0:   #check is its odd only then choc count
            if i == 0:  #if its first element then append same val
                output.append(v)
            else:
                v = v + output[i-1]
                output.append(v) 
        elif v%2 == 0: #check is its even then value as last val
            if i == 0: #if its first element then append 0
                output.append(0)
            else:
                v = output[i-1]
                output.append(v)
    return output


q01_chocolates(input_list)





