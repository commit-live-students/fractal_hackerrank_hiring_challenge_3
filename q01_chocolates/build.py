

input_list = []

# Write your solution here:


def q01_chocolates(my_list=input_list):

    val = 0
    final_list = []

    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            final_list.append(val)
        else:
            my_list[i] % 2 != 0
            val += my_list[i]
            final_list.append(val)
    return final_list


