# %load q01_chocolates/build.py


input_list= [2, 5, 8, 11, 4]


# Write your solution here:


def q01_chocolates(my_list=input_list):
    list2=list()
    newval=0
    if len(my_list)%2==0:
        for index,num in enumerate(my_list):
            if index%2==0:
                newval=num+newval
            else:
                newval=list2[index-1]
            list2.append(newval)
    else:
            for index,num in enumerate(my_list):
                if index%2!=0:
                    newval=num+newval
                else:
                    if index==0:
                        newval=0
                    else:
                        newval=list2[index-1]
                list2.append(newval)
    return(list2)
        
q01_chocolates()






