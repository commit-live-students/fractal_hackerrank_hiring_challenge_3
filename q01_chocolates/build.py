# %load q01_chocolates/build.py

input_list = [1,2,5,8]

# Write your solution here:


def q01_chocolates(my_list=input_list):
    out=[]
    count = 0
    for i in my_list:
       
        print(count)
        if count ==0 :
            if i%2 != 0 :
                out.append(i)
            else:
                out.append(0)
            count = count +1
        elif i%2 != 0:
            out.append(out[count-1] + i)
            count=count+1
        elif i%2 == 0:            
            out.append(out[count-1] )
            count=count+1
    return out    
 





