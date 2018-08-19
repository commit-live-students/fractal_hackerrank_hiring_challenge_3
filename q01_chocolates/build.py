# %load q01_chocolates/build.py


input_list = [2, 5, 8, 11, 4]

# Write your solution here:


def q01_chocolates(my_list=input_list):
    chocolate_count = 0
    chocolate_count_list = []
    for index, i in enumerate(my_list):
        if my_list[index] % 2 == 0:
            chocolate_count_list.append(chocolate_count)
        else:
            chocolate_count = chocolate_count + my_list[index]
            chocolate_count_list.append(chocolate_count)
    return chocolate_count_list





