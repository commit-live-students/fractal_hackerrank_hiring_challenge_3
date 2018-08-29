# %load q01_chocolates/build.py


input_list = []

# Write your solution here:


def q01_chocolates(my_list=input_list):
    l1 = []
    for t in my_list:
        if (t%2) != 0:
            if len(l1)>0:
                l1.append(t+l1[len(l1)-1])
            else:
                l1.append(t)
        else:
            if len(l1)>0:
                l1.append(l1[len(l1)-1])
            else:
                l1.append(0)
    return l1





