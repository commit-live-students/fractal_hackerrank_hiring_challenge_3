

input_list = []

# Write your solution here:


def q01_chocolates(my_list=input_list):
    ans = []
    for i in range(0,len(my_list)):
        ans.append(0)
        if my_list[i] % 2 == 0:
            if not i == 0:
                ans[i] = ans[i-1]

        else:
            if not i == 0:
                ans[i] = my_list[i] + ans[i-1]

            else:
                ans[i] = my_list[i]

    return ans
