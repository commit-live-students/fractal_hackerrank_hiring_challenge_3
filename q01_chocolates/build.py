#%load q01_chocolates/build.py

def q01_chocolates(input_list):

#li=[3,4,5,8,9,10]

#l#i1=[x for x in li if x%2!=0 else 
    a=[]
    tot=0
    for x ,y in enumerate(input_list) :
        if y%2!=0:
        #print(y)
            tot=tot+y
        #print(tot)
            a.append(tot)
    
        else:
            a.append(tot)
    
    #print(a)
    
    return a


q01_chocolates([3,4,5,8,9,10])        
        

    






