input_list=[1,2,5,8]
def q01_chocolates(my_list=input_list): 
    x=0
    output_list=[]
    for index in my_list:
        if index %2 !=0:
            x+=index
        output_list.append(x)
    return output_list
q01_chocolates(input_list)


