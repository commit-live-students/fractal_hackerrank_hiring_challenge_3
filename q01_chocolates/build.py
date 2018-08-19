import sys
#my_list = sys.argv[1]
my_list = [3, 4, 5, 8, 9, 10]
#days = [2, 5, 8, 11, 4]
def q01_chocolates(my_list):
    count = 0
    l = []
    for i in my_list:
        if i%2 != 0:
            l.append(i+count)
            count = i+count

        else:
            l.append(count)

    return l

print(q01_chocolates(my_list))
