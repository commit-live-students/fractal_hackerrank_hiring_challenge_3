# %load q01_chocolates/build.py


# Write your solution here:


def q01_chocolates(input_list):
    x=0
    chocolates_bought=[]
    for i in range(len(input_list)):
        if input_list[0]%2!=0:
            if i%2==0:
                x+=input_list[i]
            chocolates_bought.append(x)
        else:
            if i%2!=0:
                x+=input_list[i]
            chocolates_bought.append(x)
    return chocolates_bought
q01_chocolates([3, 4, 5, 8, 9, 10])


