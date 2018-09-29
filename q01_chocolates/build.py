# %load q01_chocolates/build.py


#input_list = [1,2,5,8]
input_list = [3, 4, 5, 8, 9, 10]
# Write your solution here:


def q01_chocolates(my_list=input_list):
    l = []
    p =0
    for element in my_list:
        if element % 2 == 1:
            p = p + element
            l.append(p)
        else:
            l.append(p)
    return l
q01_chocolates()



