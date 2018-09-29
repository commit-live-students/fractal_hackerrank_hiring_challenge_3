# %load q01_chocolates/build.py


input_list = []

# Write your solution here:


def q01_chocolates(my_list=input_list):
    #if the pos of list = odd do not consider
    #if pos is even, get the number, and add it:
    counter = 0
    new_list = []
    if len(my_list)%2==0:
        for i in range(len(my_list)):
            if i%2==0:
                counter +=my_list[i]
                new_list.append(counter)
            else:
                new_list.append(counter)
        return new_list
    else:
        for i in range(len(my_list)):
            if i%2!=0:
                counter +=my_list[i]
                new_list.append(counter)
            else:
                new_list.append(counter)
        return new_list









