# %load q01_chocolates/build.py


#input_list = [1,2,5,8]
input_list = [1,2,5,8]
# Write your solution here:


def q01_chocolates(my_list=input_list):
    
    result_list = [] #empty list for number of element
    previous_number =0 
    
    for element in my_list:
        if element % 2 == 1: #condition to test element is odd
            previous_number = previous_number + element
        
        result_list.append(previous_number) #append the result
    
    return result_list

q01_chocolates()
l = []
p = [l.append( element)if element%2 ==1 else l.append(l[len(l)-1]) for element in input_list   ]



