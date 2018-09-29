input_list = [3, 4, 5, 8, 9, 10]

def q01_chocolates(my_list=input_list):
    list2 = []
    values = 0
    for item in my_list:
        if item%2 !=0:
            values +=item
        
        list2.append(values)
    
    return list2













