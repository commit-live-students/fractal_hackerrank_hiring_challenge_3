# %load q01_chocolates/build.py


input_list = []

# Write your solution here:


def q01_chocolates(my_list=input_list):
    output_list = []
    total = 0
    for i in my_list:
        if(i%2==0):
            pass
        else:
            total = total + i
        print('Appending {}'.format(total))
        output_list.append(total)
    return output_list







