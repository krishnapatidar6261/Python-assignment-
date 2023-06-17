#Write a Python function that takes a list and returns a new list with unique elements of the first list.

def l(l1):
    l2=[]
    
    for i in l1:
        
        if i not in l2:
            
            l2.append(i)
    print(l2)
l1=["Krishna",1,2,3,4,5,2,3,4,6,8,"aashish"]            
l(l1)
