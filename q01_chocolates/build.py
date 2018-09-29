# %load q01_chocolates/build.py


input_list = []

# Write your solution here:


def q01_chocolates(my_list=input_list):
    l = []
    for i in my_list:
        
        if i%2==1:
            if not l:
                l.append(i)
            else:
                l.append(l[-1]+i)
            
        elif not l:
            l.append(0)
        else:
            l.append(l[-1])
                
    return l            
q01_chocolates([2,4,8,9,10])


